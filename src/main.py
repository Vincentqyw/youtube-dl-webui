import argparse
import yaml
import yt_dlp
import gradio as gr

def load_config(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data

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

# @title YouTube Video Downloader
# This app downloads YouTube videos using yt_dlp
# config is no use here, just for compatibility
def run(config):
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

    demo.launch(share=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path',type=str, default='config.yaml',
                            help='configuration file path')
    args = parser.parse_args()
    config = load_config(args.config_path)
    run(config)