"""inline animation function that allows rendering on github
 preview and showing click to download gif button"""

#pylint: disable=consider-using-wtih
import os
import tempfile
import base64
import imageio
import matplotlib.pyplot as plt
from IPython.display import HTML, display
from open_atmos_jupyter_utils.temporary_file import TemporaryFile


def show_anim(plot_func, frame_range, duration=0.01, loop=0):
    """plot_func is called with one argument - the frame number from frame_range
    and is expected to return a matplotlib figure instance (on which savefig()
    and close() are subsequently called)"""
    gif_file = TemporaryFile(suffix=".gif")
    with tempfile.TemporaryDirectory() as tmpdirname:
        for frame in frame_range:
            fig = plot_func(frame)
            fig.savefig(f"{tmpdirname}/{frame:05d}.png")
            plt.close(fig)
        __merge_images_into_gif(tmpdirname, gif_file, duration, loop)

        b64 = base64.b64encode(open(gif_file.basename,'rb').read()).decode("ascii")
        display(HTML(f'<img src="data:image/gif;base64,{b64}" />'))
        display(gif_file.make_link_widget())


def __merge_images_into_gif(image_folder, gif_name, duration, loop):
    """creates a GIF file from a series of animation frames"""
    with imageio.get_writer(
        gif_name.basename, duration=duration, loop=loop, mode="I"
    ) as writer:
        for filename in sorted(os.listdir(image_folder)):
            image = imageio.v3.imread(os.path.join(image_folder, filename))
            writer.append_data(image)
