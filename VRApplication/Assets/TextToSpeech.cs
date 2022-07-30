using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using com.tls;
using System;

public class TextToSpeech :MonoBehaviour
{
    private AndroidJavaClass instance=null;
    private List<string> localesList = new List<string>();
    private List<string> localescountryList = new List<string>();
    private List<string> voicesList = new List<string>();
    private AndroidJavaObject currentVoice=null;
    private AndroidJavaObject currentLocale=null;
    private string malevoice = "";
    IEnumerator Start()
    {
        yield return new WaitForSeconds(0.2f);
        initialize();
    }
    public void initialize()
    {
        var obj = instance.CallStatic<AndroidJavaObject>("getVoices");
        var rawobj = obj.GetRawObject();
        var count = AndroidJNI.GetArrayLength(rawobj);
        for (int i = 0; i < count; i++)
        {
            try
            {
                IntPtr ptrobj = AndroidJNI.GetObjectArrayElement(rawobj, i);
                var classobj = AndroidJNI.GetObjectClass(ptrobj);
                var meth = AndroidJNIHelper.GetMethodID(classobj, "toString");
                string str = AndroidJNI.CallStringMethod(ptrobj, meth, new jvalue[] { });
                voicesList.Add(str);
            }
            catch(Exception e)
            {
                Debug.Log(e.ToString());
            }
        }
        obj = instance.CallStatic<AndroidJavaObject>("getLocales");
        rawobj = obj.GetRawObject();
        count = AndroidJNI.GetArrayLength(rawobj);
        for (int i = 0; i < count; i++)
        {
            try
            {
                IntPtr ptrobj = AndroidJNI.GetObjectArrayElement(rawobj, i);
                var classobj = AndroidJNI.GetObjectClass(ptrobj);
                var meth = AndroidJNIHelper.GetMethodID(classobj, "toString");
                string str = AndroidJNI.CallStringMethod(ptrobj, meth, new jvalue[] { });
                localesList.Add(str);
            }
            catch (Exception e)
            {
                Debug.Log(e.ToString());
            }
        }
        obj = instance.CallStatic<AndroidJavaObject>("getLocalesCountries");
        rawobj = obj.GetRawObject();
        count = AndroidJNI.GetArrayLength(rawobj);
        for (int i = 0; i < count; i++)
        {
            try
            {
                IntPtr ptrobj = AndroidJNI.GetObjectArrayElement(rawobj, i);
                var classobj = AndroidJNI.GetObjectClass(ptrobj);
                var meth = AndroidJNIHelper.GetMethodID(classobj, "toString");
                string str = AndroidJNI.CallStringMethod(ptrobj, meth, new jvalue[] { });
                localescountryList.Add(str);
            }
            catch (Exception e)
            {
                Debug.Log(e.ToString());
            }
        }
        malevoice="en-in-x-cxx#male-local";
    }
    public TextToSpeech()
    {
        try
        {
            instance = TTS.GetTTSClass("com.tls.tts.TLSTextToSpeech");
        }
        catch (System.Exception ex)
        {
            Debug.Log(ex.ToString());
        }
        //currentLocale = instance.CallStatic<AndroidJavaObject>("getLocale");
        //currentLocale = instance.CallStatic<AndroidJavaObject>("getLocale");
    }
    public void Speak(string text, string utteranceid)
    {
        if (instance!=null)
        {
            instance.CallStatic("Speak", new object[] { text, utteranceid });
        }
        else
        {
            instance = TTS.GetTTSClass("com.tls.tts.TLSTextToSpeech");
            Speak(text, utteranceid);
        }
    }
    public void Speak(object[] param)
    {
        instance.CallStatic("Speak", param);
        //getCurrentLocale();
        //getCurrentVoice();
    }
    public bool isSpeaking()
    {
        bool value;
        value = instance.CallStatic<bool>("isSpeaking");
        return value;
    }
    public void getCurrentVoice()
    {
        currentVoice = instance.CallStatic<AndroidJavaObject>("getVoice");
        var mess = currentVoice.GetStatic<string>("getName");
        TTS.Toast(mess);
    }
    public void getCurrentLocale()
    {
        currentLocale = instance.CallStatic<AndroidJavaObject>("getLocale");
        var mess = currentLocale.GetStatic<string>("getDisplayLanguage") + " | " + currentLocale.GetStatic<string>("getDisplayCountry");
        TTS.Toast(mess);
    }
    public List<string> getLocales()
    {
        var locales = new List<string>();
        var obj = instance.CallStatic<AndroidJavaObject>("getLocalesNames");
        var rawobj = obj.GetRawObject();
        var count = AndroidJNI.GetArrayLength(rawobj);
        for (int i = 0; i < count; i++)
        {
            try
            {
                IntPtr ptrobj = AndroidJNI.GetObjectArrayElement(rawobj, i);
                var classobj = AndroidJNI.GetObjectClass(ptrobj);
                var meth = AndroidJNIHelper.GetMethodID(classobj, "toString");
                string str = AndroidJNI.CallStringMethod(ptrobj, meth, new jvalue[] { });
                locales.Add(str);
            }
            catch (Exception e)
            {
                Debug.Log(e.ToString());
            }
        }
        return locales;
    }

    public void setLocale(int position)
    {
        var lang = localesList[position];
        var cont = localescountryList[position];
        instance.CallStatic("setupLocale",new object[] {lang,cont});
    }
    public void setLocale(string lang, string cont)
    {
        instance.CallStatic("setupLocale", new object[] { lang, cont });
    }
    public void setVoice(string name)
    {
        instance.CallStatic("setupVoice", new object[] { name});
    }
    public List<string> getVoices() {
        var voices = new List<string>();
        var obj = instance.CallStatic<AndroidJavaObject>("getVoices");
        var rawobj = obj.GetRawObject();
        var count = AndroidJNI.GetArrayLength(rawobj);
        for (int i = 0; i < count; i++)
        {
            try
            {
                IntPtr ptrobj = AndroidJNI.GetObjectArrayElement(rawobj, i);
                var classobj = AndroidJNI.GetObjectClass(ptrobj);
                var meth = AndroidJNIHelper.GetMethodID(classobj, "toString");
                string str = AndroidJNI.CallStringMethod(ptrobj, meth, new jvalue[] { });
                voices.Add(str);
            }
            catch (Exception e)
            {
                Debug.Log(e.ToString());
            }
        }
        return voices;
    }
}
