# video-subtitler
A tool for automatically captioning your .mp4 files, based on STT

## Design
The tool will feature a web page implementing a drag + drop menu for uploading an MP4 file.
Backend will use some library to process the video and add captions to it.
The webpage will return the video as a downloadable. Future versions might feature a "preview" page.


## Implementation Steps
- [ ] Start by building a CLI tool that receives an MP4 file as input, processes and returns a captioned video
- [ ] Implement wrapper (with Flask) to access the tool via HTTP
- [ ] Create frontend webserver (still need to think of tools for that) with drag & drop inputting
