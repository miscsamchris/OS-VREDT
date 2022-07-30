using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WitAI : MonoBehaviour
{
    public string authentication, version;
    public SpeechManager sm;
    public void send(string query)
    {
        Dictionary<string, string> headers = new Dictionary<string, string>();
        headers.Add("Context-Type", "application/json");
        headers.Add("Authorization", authentication);
        WWW www = new WWW("https://api.wit.ai/message?v=" + version + "&q=" + query + "", null, headers);
        StartCoroutine(GetDataSpeech(www));
    }
    public IEnumerator GetDataSpeech(WWW request)
    {
        yield return request;
        if (request.error != null)
        {
            Debug.Log("error: " + request.error);
            Debug.Log("error: " + request.text);
        }
        else
        {
            sm.JsonSuccess(request.text);
        }
    }
}
