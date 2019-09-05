using UnityEngine;

namespace MLAgents
{
    public class FlyCamera : MonoBehaviour
    {
        /*
        WASD : basic movement
        shift : Makes camera accelerate
        space : Moves camera on X and Z axis only.  So camera doesn't gain any height*/


        public float mainSpeed = 100.0f; // regular speed
        public float shiftAdd = 250.0f; // multiplied by how long shift is held.  Basically running
        public float maxShift = 1000.0f; // Maximum speed when holdin gshift
        public float camSens = 0.25f; // How sensitive it with mouse
        public bool rotateOnlyIfMousedown = true;
        public bool movementStaysFlat = true;

        private Vector3
            m_LastMouse =
            new Vector3(255, 255,
                255);     // kind of in the middle of the screen, rather than at the top (play)

        private float m_TotalRun = 1.0f;

        void Awake()
        {
            Debug.Log("FlyCamera Awake() - RESETTING CAMERA POSITION"); // nop?
            // nop:
            // transform.position.Set(0,8,-32);
            // transform.rotation.Set(15,0,0,1);
            transform.position = new Vector3(0, 8, -32);
            transform.rotation = Quaternion.Euler(25, 0, 0);
        }

        void Update()
        {
            if (Input.GetMouseButtonDown(1))
            {
                m_LastMouse = Input.mousePosition; // $CTK reset when we begin
            }

            Transform myTransform;
            if (!rotateOnlyIfMousedown ||
                (rotateOnlyIfMousedown && Input.GetMouseButton(1)))
            {
                m_LastMouse = Input.mousePosition - m_LastMouse;
                m_LastMouse = new Vector3(-m_LastMouse.y * camSens, m_LastMouse.x * camSens, 0);
                myTransform = transform;
                var eulerAngles = myTransform.eulerAngles;
                m_LastMouse = new Vector3(eulerAngles.x + m_LastMouse.x,
                    eulerAngles.y + m_LastMouse.y, 0);
                eulerAngles = m_LastMouse;
                myTransform.eulerAngles = eulerAngles;
                m_LastMouse = Input.mousePosition;
                // Mouse  camera angle done.
            }

            // Keyboard commands
            var p = GetBaseInput();
            if (Input.GetKey(KeyCode.LeftShift))
            {
                m_TotalRun += Time.deltaTime;
                p = shiftAdd * m_TotalRun * p;
                p.x = Mathf.Clamp(p.x, -maxShift, maxShift);
                p.y = Mathf.Clamp(p.y, -maxShift, maxShift);
                p.z = Mathf.Clamp(p.z, -maxShift, maxShift);
            }
            else
            {
                m_TotalRun = Mathf.Clamp(m_TotalRun * 0.5f, 1f, 1000f);
                p *= mainSpeed;
            }

            p *= Time.deltaTime;
            myTransform = transform;
            var newPosition = myTransform.position;
            if (Input.GetKey(KeyCode.Space)
                || movementStaysFlat && !(rotateOnlyIfMousedown && Input.GetMouseButton(1)))
            {
                // If player wants to move on X and Z axis only
                myTransform.Translate(p);
                var position = myTransform.position;
                newPosition.x = position.x;
                newPosition.z = position.z;
                position = newPosition;
                myTransform.position = position;
            }
            else
            {
                transform.Translate(p);
            }
        }

        private static Vector3 GetBaseInput()
        {
            // returns the basic values, if it's 0 than it's not active.
            var pVelocity = new Vector3();
            if (Input.GetKey(KeyCode.W))
            {
                pVelocity += new Vector3(0, 0, 1);
            }

            if (Input.GetKey(KeyCode.S))
            {
                pVelocity += new Vector3(0, 0, -1);
            }

            if (Input.GetKey(KeyCode.A))
            {
                pVelocity += new Vector3(-1, 0, 0);
            }

            if (Input.GetKey(KeyCode.D))
            {
                pVelocity += new Vector3(1, 0, 0);
            }

            return pVelocity;
        }
    }
}
