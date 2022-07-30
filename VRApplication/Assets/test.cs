using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class test : MonoBehaviour
{
    public TextToSpeech t;
    public SpeechToText s;
    public Text text;
    public InputField inp;
    public Dropdown localeDrop;
    private void Awake()
    {
        try
        {
            t = new TextToSpeech();
            s = new SpeechToText(transform.name, "settext");
        }
        catch (System.Exception ex)
        {
            Debug.Log(ex.ToString());
        }
    }
    IEnumerator Start()
    {
        yield return new WaitForSeconds(0.5f);
        var los = t.getLocales();
        foreach (var option in los)
        {
            localeDrop.options.Add(new Dropdown.OptionData(option));
        }
    }
    public void onset_locale(Dropdown drop)
    {
        var position = drop.value;
        t.setLocale(position);
    }
    public void onclick_speak()
    {
        t.Speak(inp.text, "Hello");
    }
    public void onclick_speaking()
    {
        text.text = t.isSpeaking().ToString();
    }
    public void onclick_SpeechRecognition()
    {
        s.StartRecognition();
    }
    public void settext(string str)
    {
        text.text = str;
        if (str=="set new language")
        {
            s.setLocale("ta", "in");
        }
    }
}
