using System.Collections;
using UnityEngine;
 
namespace com.tls
{
    class TTS
    {
        public static AndroidJavaClass GetTTSClass(string androidJavaClass)
        {
            AndroidJavaClass result=null;

            //Only works on Android!
            if (Application.platform == RuntimePlatform.Android)
            {
                try
                {
                    result = new AndroidJavaClass(androidJavaClass);
                    if (null != result)
                    {
                        AndroidJavaClass unityPlayer = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
                        AndroidJavaObject activity = unityPlayer.GetStatic<AndroidJavaObject>("currentActivity");
                        AndroidJavaObject context = activity.Call<AndroidJavaObject>("getApplicationContext");
                        result.CallStatic("setContext",context);
                    }
                    else
                    {
                        Debug.Log("Result is Null");
                    }
                }
                catch (System.Exception ex)
                {
                    Debug.Log(string.Format("{0} Exception:{1}", ex.StackTrace, ex.ToString()));
                }

            }
                return result;
        }
        public static AndroidJavaClass GetSpeechClass(string androidJavaClass,string name,string func)
        {
            AndroidJavaClass result = null;

            //Only works on Android!
            if (Application.platform == RuntimePlatform.Android)
            {
                try
                {
                    result = new AndroidJavaClass(androidJavaClass);
                    if (null != result)
                    {
                        AndroidJavaClass unityPlayer = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
                        AndroidJavaObject activity = unityPlayer.GetStatic<AndroidJavaObject>("currentActivity");
                        AndroidJavaObject context = activity.Call<AndroidJavaObject>("getApplicationContext");
                        activity.Call("runOnUiThread", new AndroidJavaRunnable(() => {
                            result.CallStatic("setContext", context, name, func);
                        }));
                    }
                    else
                    {
                        Debug.Log("Result is Null");
                    }
                }
                catch (System.Exception ex)
                {
                    Debug.Log(string.Format("{0} Exception:{1}", ex.StackTrace, ex.ToString()));
                }

            }
            return result;
        }
        public static void Toast(string message)
        {
            AndroidJavaClass unityPlayer = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
            AndroidJavaObject unityActivity = unityPlayer.GetStatic<AndroidJavaObject>("currentActivity");

            if (unityActivity != null)
            {
                AndroidJavaClass toastClass = new AndroidJavaClass("android.widget.Toast");
                unityActivity.Call("runOnUiThread", new AndroidJavaRunnable(() =>
                {
                    AndroidJavaObject toastObject = toastClass.CallStatic<AndroidJavaObject>("makeText", unityActivity,
                        message, 0);
                    toastObject.Call("show");
                }));
            }
        }
    }
}

