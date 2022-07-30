using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class VideoDataLoader : MonoBehaviour
{
    public Dropdown VideoDropDown;
    public Text vid,vname, vdes, tname, tdes,Video_Label;
    private string topicname, topicdesc;
    public GameObject Screen;
    public WitAI wit;
    private videoplay vidplay;

    private void Start()
    {
        vidplay = Screen.GetComponent<videoplay>();
    }
    public void ChangeVideos(string name)
    {
        WWW req = new WWW("https://osvredt.herokuapp.com/rest/topic/" + name + "/");
        StartCoroutine(ChangeVideo(req));
    }
    public IEnumerator ChangeVideo(WWW req)
    {
        yield return req;
        if (req.text.Length >= 5)
        {
            JSONObject a = new JSONObject(req.text);
            if (a.GetField("code").ToString() == "200")
            {
                topicname= a.GetField("Topic Name").ToString();
                topicdesc = a.GetField("Description").ToString();
                VideoDropDown.options.Clear();
                var list = a.GetField("Videos");
                VideoDropDown.options.Add(new Dropdown.OptionData("Select Video"));
                for (int i = 0; i < list.Count; i++)
                {
                    var itemid = list[i].GetField("Video ID").ToString();
                    var item = list[i].GetField("Video Name").ToString();
                    item = itemid + "." + item.Substring(1, item.Length - 2);
                    VideoDropDown.options.Add(new Dropdown.OptionData(item));
                }
                VideoDropDown.value = 0;
                Video_Label.text = "Select Video";
                OnVideoChange();
                var cblist = a.GetField("Chatbots");
                for (int i = 0; i < cblist.Count; i++)
                {
                    var cbid = cblist[i].GetField("chatbot_access_code").ToString();
                    wit.authentication = "Bearer " + cbid;
                }
            }
        }
    }
    public void OnVideoChange()
    {
        var video = VideoDropDown.value;
        var videoname = VideoDropDown.options[video].text;
        videoname = videoname.Substring(videoname.IndexOf('.') + 1);
        WWW req = new WWW("https://osvredt.herokuapp.com/rest/video/name/" + videoname + "/");
        StartCoroutine(ChangeVideoDetails(req));
    }
    public void OnClickPlay()
    {
        var videoid = vid.text;
        var videoname = vname.text;
        videoname = videoname.Replace(' ','_')+".mp4";
        print(videoid);
        var url = "https://osvredt.herokuapp.com/video/stream/" + videoid+"/";
        vidplay.setvideoURL(url,videoname);
        print(url + "From onclick");
    }
    public void OnClickScreen(Text t)
    {
        if (!vidplay.cp.isPlaying)
        {
            vidplay.cp.Play();
            t.text = "Pause";
        }
        else
        {
            vidplay.cp.Pause();
            t.text = "Play";
        }
    }
    public IEnumerator ChangeVideoDetails(WWW req)
    {
        yield return req;
        if (req.text.Length >= 5)
        {
            JSONObject a = new JSONObject(req.text);
            if (a.GetField("code").ToString() == "200")
            {
                var videoid= a.GetField("id").ToString();
                var videoname = a.GetField("Video Name").ToString();
                var videodesc = a.GetField("Description").ToString();
                vid.text = videoid;
                vname.text = videoname.Substring(1, videoname.Length - 2);
                vdes.text = videodesc.Substring(1, videodesc.Length - 2); ;
                tname.text = topicname.Substring(1, topicname.Length - 2); ;
                tdes.text = topicdesc.Substring(1, topicdesc.Length - 2); ;
                Video_Label.text = videoname.Substring(1, videoname.Length - 2); ;
            }
        }
    }
}
