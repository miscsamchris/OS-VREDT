using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using com.tls;

public class SpeechToText : MonoBehaviour
{
    private AndroidJavaClass instance = null;
    public SpeechToText(string name, string func)
    {
        try
        {
            instance = TTS.GetSpeechClass("com.tls.tts.TLSSpeechToText", name,func);
        }
        catch (System.Exception ex)
        {
            Debug.Log(ex.ToString());
        }
    }
    IEnumerator Start()
    {
        yield return new WaitForSeconds(0.2f);

    }

    public void StartRecognition()
    {
        AndroidJavaClass unityPlayer = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
        AndroidJavaObject activity = unityPlayer.GetStatic<AndroidJavaObject>("currentActivity");
        activity.Call("runOnUiThread", new AndroidJavaRunnable(() => {
            instance.CallStatic("StartRecognition");
        }));
    }
    public void setLocale(string lang, string cont)
    {
        instance.CallStatic("addExtraLanguage", new object[] { lang,cont });
    }
}
