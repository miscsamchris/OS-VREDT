using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.Video;

public class videoplay : MonoBehaviour
{

    public VideoPlayer cp;
    public AudioSource aus;
    private string videoFile;
    void Start()
    {
        cp = gameObject.GetComponent<VideoPlayer>();
        cp.playOnAwake = false;
        aus = gameObject.GetComponent<AudioSource>();
        aus.playOnAwake = false;
        cp.source = VideoSource.Url;
    }

    public void setvideoURL(string s,string videoname)
    {
        videoFile = Application.persistentDataPath + "/"+videoname;
        StartCoroutine(DownloadAndPlayVideo(s));

    }
    IEnumerator DownloadAndPlayVideo(string url)
    {
        if (!File.Exists(videoFile))
        {
            WWW www = new WWW(url);

            yield return www;

            if (www != null && www.isDone && www.error == null)
            {
                FileStream stream = new FileStream(videoFile, FileMode.Create);
                stream.Write(www.bytes, 0, www.bytes.Length);
                stream.Close();

            }

        }
        string playVideoFile = "file://" + videoFile;
        LoadVideo(url);
    }

    public void LoadVideo(string s)
    {
        cp.url = s;
        cp.audioOutputMode = VideoAudioOutputMode.AudioSource;
        cp.EnableAudioTrack(0, true);
        cp.SetTargetAudioSource(0, aus);
        cp.Prepare();
    }

}
