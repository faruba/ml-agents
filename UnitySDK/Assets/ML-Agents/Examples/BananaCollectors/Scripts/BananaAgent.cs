using UnityEngine;
using MLAgents;

[RequireComponent(typeof(Rigidbody))]
public class BananaAgent : Agent
{
    private BananaAcademy m_MyAcademy;
    public GameObject area;
    BananaArea m_MyArea;
    bool m_Frozen;
    bool m_Poisoned;
    bool m_Satiated;
    bool m_Shoot;
    float m_FrozenTime;
    float m_EffectTime;
    Rigidbody m_AgentRb;
    private float m_LaserLength;
    // Speed of agent rotation.
    public float turnSpeed = 300;

    // Speed of agent movement.
    public float moveSpeed = 2;
    public Material normalMaterial;
    public Material badMaterial;
    public Material goodMaterial;
    public Material frozenMaterial;
    public GameObject myLaser;
    public bool contribute;
    private RayPerception3D m_RayPer;
    public bool useVectorObs;


    public override void InitializeAgent()
    {
        base.InitializeAgent();
        m_AgentRb = GetComponent<Rigidbody>();
        Monitor.verticalOffset = 1f;
        m_MyArea = area.GetComponent<BananaArea>();
        m_RayPer = GetComponent<RayPerception3D>();
        m_MyAcademy = FindObjectOfType<BananaAcademy>();

        SetResetParameters();
    }

    protected override void CollectObservations()
    {
        if (useVectorObs)
        {
            float rayDistance = 50f;
            float[] rayAngles = { 20f, 90f, 160f, 45f, 135f, 70f, 110f };
            string[] detectableObjects = { "banana", "agent", "wall", "badBanana", "frozenAgent" };
            AddVectorObs(m_RayPer.Perceive(rayDistance, rayAngles, detectableObjects, 0f, 0f));
            Vector3 localVelocity = transform.InverseTransformDirection(m_AgentRb.velocity);
            AddVectorObs(localVelocity.x);
            AddVectorObs(localVelocity.z);
            AddVectorObs(System.Convert.ToInt32(m_Frozen));
            AddVectorObs(System.Convert.ToInt32(m_Shoot));
        }
    }

    void MoveAgent(float[] act)
    {
        m_Shoot = false;

        if (Time.time > m_FrozenTime + 4f && m_Frozen)
        {
            Unfreeze();
        }
        if (Time.time > m_EffectTime + 0.5f)
        {
            if (m_Poisoned)
            {
                Unpoison();
            }
            if (m_Satiated)
            {
                Unsatiate();
            }
        }

        var dirToGo = Vector3.zero;
        var rotateDir = Vector3.zero;

        if (!m_Frozen)
        {
            var shootCommand = false;
            if (brain.brainParameters.vectorActionSpaceType == SpaceType.Continuous)
            {
                dirToGo = transform.forward * Mathf.Clamp(act[0], -1f, 1f);
                rotateDir = transform.up * Mathf.Clamp(act[1], -1f, 1f);
                shootCommand = Mathf.Clamp(act[2], -1f, 1f) > 0.5f;
            }
            else
            {
                var forwardAxis = (int)act[0];
                var rightAxis = (int)act[1];
                var rotateAxis = (int)act[2];
                var shootAxis = (int)act[3];

                switch (forwardAxis)
                {
                    case 1:
                        dirToGo = transform.forward;
                        break;
                    case 2:
                        dirToGo = -transform.forward;
                        break;
                }

                switch (rightAxis)
                {
                    case 1:
                        dirToGo = transform.right;
                        break;
                    case 2:
                        dirToGo = -transform.right;
                        break;
                }

                switch (rotateAxis)
                {
                    case 1:
                        rotateDir = -transform.up;
                        break;
                    case 2:
                        rotateDir = transform.up;
                        break;
                }
                switch (shootAxis)
                {
                    case 1:
                        shootCommand = true;
                        break;
                }
            }
            if (shootCommand)
            {
                m_Shoot = true;
                dirToGo *= 0.5f;
                m_AgentRb.velocity *= 0.75f;
            }
            m_AgentRb.AddForce(dirToGo * moveSpeed, ForceMode.VelocityChange);
            transform.Rotate(rotateDir, Time.fixedDeltaTime * turnSpeed);
        }

        if (m_AgentRb.velocity.sqrMagnitude > 25f) // slow it down
        {
            m_AgentRb.velocity *= 0.95f;
        }

        if (m_Shoot)
        {
            myLaser.transform.localScale = new Vector3(1f, 1f, m_LaserLength);
            Transform transform1;
            var position = (transform1 = transform).TransformDirection(RayPerception3D.PolarToCartesian(25f, 90f));
            Debug.DrawRay(transform1.position, position, Color.red, 0f, true);
            RaycastHit hit;
            if (Physics.SphereCast(transform.position, 2f, position, out hit, 25f))
            {
                if (hit.collider.gameObject.CompareTag("agent"))
                {
                    hit.collider.gameObject.GetComponent<BananaAgent>().Freeze();
                }
            }
        }
        else
        {
            myLaser.transform.localScale = new Vector3(0f, 0f, 0f);
        }
    }

    void Freeze()
    {
        gameObject.tag = "frozenAgent";
        m_Frozen = true;
        m_FrozenTime = Time.time;
        gameObject.GetComponent<Renderer>().material = frozenMaterial;
    }

    void Unfreeze()
    {
        m_Frozen = false;
        gameObject.tag = "agent";
        gameObject.GetComponent<Renderer>().material = normalMaterial;
    }

    void Poison()
    {
        m_Poisoned = true;
        m_EffectTime = Time.time;
        gameObject.GetComponent<Renderer>().material = badMaterial;
    }

    void Unpoison()
    {
        m_Poisoned = false;
        gameObject.GetComponent<Renderer>().material = normalMaterial;
    }

    void Satiate()
    {
        m_Satiated = true;
        m_EffectTime = Time.time;
        gameObject.GetComponent<Renderer>().material = goodMaterial;
    }

    void Unsatiate()
    {
        m_Satiated = false;
        gameObject.GetComponent<Renderer>().material = normalMaterial;
    }

    public override void AgentAction(float[] vectorAction, string textAction)
    {
        MoveAgent(vectorAction);
    }

    public override void AgentReset()
    {
        Unfreeze();
        Unpoison();
        Unsatiate();
        m_Shoot = false;
        m_AgentRb.velocity = Vector3.zero;
        myLaser.transform.localScale = new Vector3(0f, 0f, 0f);
        transform.position = new Vector3(Random.Range(-m_MyArea.range, m_MyArea.range),
            2f, Random.Range(-m_MyArea.range, m_MyArea.range))
            + area.transform.position;
        transform.rotation = Quaternion.Euler(new Vector3(0f, Random.Range(0, 360)));

        SetResetParameters();
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("banana"))
        {
            Satiate();
            collision.gameObject.GetComponent<BananaLogic>().OnEaten();
            AddReward(1f);
            if (contribute)
            {
                m_MyAcademy.totalScore += 1;
            }
        }
        if (collision.gameObject.CompareTag("badBanana"))
        {
            Poison();
            collision.gameObject.GetComponent<BananaLogic>().OnEaten();

            AddReward(-1f);
            if (contribute)
            {
                m_MyAcademy.totalScore -= 1;
            }
        }
    }

    public override void AgentOnDone()
    {
    }

    public void SetLaserLengths()
    {
        m_LaserLength = m_MyAcademy.resetParameters["laser_length"];
    }

    public void SetAgentScale()
    {
        var agentScale = m_MyAcademy.resetParameters["agent_scale"];
        gameObject.transform.localScale = new Vector3(agentScale, agentScale, agentScale);
    }

    public void SetResetParameters()
    {
        SetLaserLengths();
        SetAgentScale();
    }
}
