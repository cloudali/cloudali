# Hi there 👋, I'm Ali

![visitor badge](https://visitor-badge.laobi.icu/badge?page_id=cloudali.visitor-badge&left_color=red&right_color=green&left_text=hello_Visitors)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

```python
import time, random, string
def docker_build():
    for step in [f"Sending build context to Docker daemon  {random.randint(1, 1024)} KB", "Step 1/3 : FROM ubuntu:18.04", "Step 2/3 : EXPOSE 80", "Step 3/3 : COPY matrix/index.html /usr/share/nginx/html/index.html", f"Successfully built {''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}", "Successfully tagged nginx:latest"]: print(step); time.sleep(0.5)
    print("----- Container Ready! Starting Application 👾 -----\n")

def welcome():
    devopsDance = """
   .aMMMb  dMP    .aMMMb  dMP dMP dMMMMb         .aMMMb  dMP     dMP 
  dMP"VMP dMP    dMP"dMP dMP dMP dMP VMP        dMP"dMP dMP     amr  
 dMP     dMP    dMP dMP dMP dMP dMP dMP        dMMMMMP dMP     dMP   
dMP.aMP dMP    dMP.aMP dMP.aMP dMP.aMP        dMP dMP dMP     dMP    
VMMMP" dMMMMMP VMMMP"  VMMMP" dMMMMP"        dMP dMP dMMMMMP dMP     
                                                                   """
    print(devopsDance)

class CloudEngineer:
    def __init__(self):
        self.name = "Ali"
        self.role = "Aspiring Software Engineer 🚀"
        self.status = ["Kubernetes", "zOS & Cobol", "SpringBoot", "and cloud infrastructure"]
        self.languages_programming = ["Python", "Java", "Go"]
        self.languages_real = ["English", "Sarcasm_JK"]
        self.website = "https://cloudali.net"

    def say_hi(self):
        print(f"Hey there ! My name is \033[35m{self.name}\033[0m, and I am an \033[35m{self.role}\033[0m.")
        print(f"I am currently learning everything about {', '.join(self.status)}.")
        print("I program primarily in {}, but also use {} from time to time.\n".format(
            self.languages_programming[0],
            ' & '.join(self.languages_programming[1:])
        ))
        print("Thanks for stopping in! I hope my profile and projects are more thrilling than your average cat video. Spoiler: they might not be!\n")
        print(f"You can find more about me and my projects 👉 \033[35m{self.website}\033[0m 👈 [CMD/CTRL + CLICK].\n")  

    def start(self):
        welcome()
        docker_build()
        self.say_hi()

me = CloudEngineer()
me.start()

# Usage - Copy the python code provided above into your text editor / IDE and run the script!
# or if you're one of the cool kids - follow the instructions to run the cool docker version below :)
```
Run an animated verison of this script locally in a docker container using my setup shell script [🔗 Docker Setup Instructions](https://github.com/cloudali/cloudali/blob/main/setup.md
)
## 📝 Links

- 🌎 Personal website and blog: https://cloudali.net

## 🗂️ Highlight Projects

<a href="https://github.com/cloudali/aws-cloud-resume">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=cloudali&repo=aws-cloud-resume&show_icons=true&line_height=27&title_color=6aa6f8&text_color=8a919a&icon_color=6aa6f8&bg_color=22272e" alt="aws-cloud-resume" />
</a>

<a href="https://github.com/cloudali/aws-cloud-resume-backend">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=cloudali&repo=aws-cloud-resume-backend&show_icons=true&line_height=27&title_color=6aa6f8&text_color=8a919a&icon_color=6aa6f8&bg_color=22272e" alt="aws-cloud-resume-backend" />
</a>
