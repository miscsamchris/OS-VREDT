using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class ContentLoader : MonoBehaviour
{
    // Start is called before the first frame update

    public Dropdown subjectdropdown,topicdropdown;
    public Text Subject_Label, Topic_Label;
    public GameObject Videomenu;
    private VideoDataLoader vdl;
    public IEnumerator request(WWW req,Dropdown d)
    {
        yield return req;
        if (req.text.Length >= 5)
        {
            JSONObject a = new JSONObject(req.text);
            if (a.GetField("code").ToString()=="200")
            {
                d.options.Clear();
                var list = a.GetField("subjects");
                d.options.Add(new Dropdown.OptionData("Select Subject"));
                for (int i = 0; i < list.Count; i++)
                {
                    var itemid = list[i].GetField("id").ToString();
                    var item = list[i].GetField("Subject Name").ToString();
                    item = itemid + "." +item.Substring(1, item.Length-2);
                    d.options.Add(new Dropdown.OptionData(item));
                }
                d.value = 0;
            }
        }
    }
    public void OnSubjectChange()
    {
        var subject = subjectdropdown.value;
        var subjectname = subjectdropdown.options[subject].text;
        subjectname = subjectname.Substring(subjectname.IndexOf('.')+1);
        Subject_Label.text = subjectname;
        WWW req = new WWW("https://osvredt.herokuapp.com/rest/subject/" + subjectname+"/");
        StartCoroutine(ChangeTopics(req));
    }
    public IEnumerator ChangeTopics(WWW req)
    {
        yield return req;
        if (req.text.Length >= 5)
        {
            JSONObject a = new JSONObject(req.text);
            if (a.GetField("code").ToString() == "200")
            {
                topicdropdown.options.Clear();
                var list = a.GetField("Topics");
                topicdropdown.options.Add(new Dropdown.OptionData("Select Topic"));
                for (int i = 0; i < list.Count; i++)
                {
                    var itemid = list[i].GetField("Topic ID").ToString();
                    var item = list[i].GetField("Topic Name").ToString();
                    item = itemid + "." + item.Substring(1, item.Length - 2);
                    topicdropdown.options.Add(new Dropdown.OptionData(item));
                }
                topicdropdown.value = 0;
            }
        }
    }
    void Start()
    {
        WWW req = new WWW("https://osvredt.herokuapp.com/rest/subject");
        StartCoroutine(request(req,subjectdropdown));
        vdl = transform.GetComponent<VideoDataLoader>();
    }
    public void OnTopicChange()
    {
        var topic = topicdropdown.value;
        var topicname = topicdropdown.options[topic].text;
        topicname = topicname.Substring(topicname.IndexOf('.')+1);
        Topic_Label.text = topicname;
        Videomenu.SetActive(true);
        vdl.ChangeVideos(topicname);
    }

    public void Refresh()
    {
        WWW req = new WWW("https://osvredt.herokuapp.com/rest/subject");
        StartCoroutine(request(req, subjectdropdown));
    }
}
