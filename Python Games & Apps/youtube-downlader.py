from pytube import YouTube

link = 'https://www.youtube.com/watch?v=FVq6TYw9WjE&list=PLuXY3ddo_8nzCVqXcTFqwcM5R0gZiMRiW&index=2'
#link =  input("Please enter the video url: ")

video = YouTube(link)

# print(f"The video title is:\n {video.title} \n ---------------------")
# print(f"The video description is:\n{video.description} \n ----------------")
# print(f"The video views are: {video.views} \n --------------------")
# print(f"The video rating is: {video.rating} \n ------------------")
# print(f"The video duration is: {video.length} \n-----------------")

# print(video.streams)

# for stream in video.streams:
#     print(stream)

# for stream in video.streams.filter(progressive=True):
#     print(stream)
#         or
# print(video.streams.get_highest_resolution())
#          or
# print(video.streams.get_lowest_resolution())


def finish():
    print("dowenload done")


video.streams.get_lowest_resolution().download(
    output_path="/home/neo/Downloads")

video.register_on_complete_callback(finish())
