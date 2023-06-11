import yt_dlp
import gradio as gr

def download_video(url, save_path, proxy = '127.0.0.1:1080'):
    ydl_opts = {
        'proxy': proxy,
        'format': 'best',
        'restrict-filenames': True,
        'outtmpl': save_path + '/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "Video downloaded successfully!"

input_url = gr.inputs.Textbox(label="Enter YouTube video URL")
output_path = gr.inputs.Textbox(label="Enter save path for video")
proxy = gr.inputs.Textbox(label="Enter Proxy",placeholder="127.0.0.1")

output_text = gr.outputs.Textbox(label="Download Status")

demo = gr.Interface(
    fn=download_video, 
    inputs=[input_url, output_path, proxy],
    outputs=output_text,
    title="YouTube Video Downloader",
    description="Download YouTube videos using yt_dlp",
    theme="compact"
)

demo.launch()
