import os
import urllib.request as request
import ssl
import plot

file_name = 'data.json'
data_url = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    response = request.urlopen(data_url)
    f = open(file_name, "w+")
    f.write(response.read().decode())
    f.close()
    plot.Drawing.draw_plots(file_name)
    os.remove(file_name)


if __name__ == '__main__':
    main()
