using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SpeechManager : MonoBehaviour
{
    private TextToSpeech speaker;
    public WitAI wit;
    private SpeechToText sp;
    public System.Func<bool> speechtest;
    public Animator CB;
    // Start is called before the first frame update
    void Awake()
    {
        try
        {
            sp = new SpeechToText(this.transform.name, "OnSTT");
            speaker = new TextToSpeech();
            speechtest = new System.Func<bool>(() => speaker.isSpeaking());
            
        }
        catch (System.Exception ex)
        {
            Debug.Log(ex.ToString());
        }
    }
    public void OnSTT(string s)
    {
        wit.send(s);
    }
    public void StartRecognition()
    {
        sp.StartRecognition();
    }
    public void Speak(string text)
    {
        speaker.Speak(text, "From "+ SceneManager.GetActiveScene().name);
    }
    public void JsonSuccess(string json)
    {
        JSONObject a = new JSONObject(json);
        var intents = a.GetField("intents");
        var count = intents.Count;
        JSONObject resolvedintent = null;
        if (count > 0)
        {
            resolvedintent = intents[0];
        }
        if (resolvedintent != null)
        {
            var intentname = resolvedintent.GetField("name").ToString();
            intentname = intentname.Replace("\"", "");
            WWW req = new WWW("https://osvredt.herokuapp.com/rest/intent/" + intentname + "/");
            StartCoroutine(GetResponse(req));
        }
    }
    public IEnumerator isspeaking()
    {
        
        CB.Play("Talk");
        yield return new WaitForSeconds(1.0f);
        yield return new WaitWhile(speechtest);
        CB.Play("Idle");
    }
    public IEnumerator GetResponse(WWW req)
    {
        yield return req;
        if (req.text.Length >= 5)
        {
            JSONObject a = new JSONObject(req.text);
            if (a.GetField("code").ToString() == "200")
            {
                string response = a.GetField("Response").ToString();
                speaker.Speak(response, "I'm Sorry. I didn't get that.");
                StartCoroutine(isspeaking());
            }
        }
    }
}
