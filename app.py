import argparse
import yaml
import yt_dlp
import gradio as gr
import yaml


def load_config(file_path):
    """
    Loads the configuration from the specified file path.

    Args:
        file_path (str): The path to the configuration file.

    Returns:
        dict: The loaded configuration data.
    """
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


# Define the function with arguments and return type annotations
def download_video(url: str, save_path: str, proxy: str = "127.0.0.1:1080") -> str:
    """
    Download a video from the given URL and save it to the specified path.

    Args:
        url (str): The URL of the video.
        save_path (str): The path where the downloaded video will be saved.
        proxy (str, optional): The proxy to be used for the download. Defaults to "127.0.0.1:1080".

    Returns:
        str: A message indicating the success of the download.
    """
    # Set the options for the YouTube downloader
    ydl_opts = {
        "proxy": proxy,
        "format": "best",
        "restrict-filenames": True,
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
    }
    
    # Create a context manager for the YouTube downloader and download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return "Video downloaded successfully!"


# @title YouTube Video Downloader
# This app downloads YouTube videos using yt_dlp
# config is no use here, just for compatibility


def main(config: dict) -> None:
    """
    Runs the YouTube Video Downloader interface.

    Args:
        config (dict): Configuration dictionary containing input_url,
        output_path, and proxy.

    Returns:
        None
    """
    config_proxy = "{}:{}".format(config["proxy"], config["port"])

    input_url = gr.Textbox(label="Enter YouTube video URL")
    output_path = gr.Textbox(
        label="Enter save path for video", placeholder=config["output_folder"]
    )
    proxy = gr.Textbox(label="Enter Proxy", placeholder=config_proxy)

    output_text = gr.Textbox(label="Download Status")

    demo = gr.Interface(
        fn=download_video,
        inputs=[input_url, output_path, proxy],
        outputs=output_text,
        title="YouTube Video Downloader",
        description="Download YouTube videos using yt_dlp",
        theme="compact",
    )

    demo.launch(share=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config_path",
        type=str,
        default="config.yaml",
        help="configuration file path",
    )
    args = parser.parse_args()
    config = load_config(args.config_path)
    main(config)
