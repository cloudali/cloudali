import time, random, string

def welcome():
    devopsDance_frames = [
        """
   .aMMMb  dMP 
  dMP"VMP dMP  
 dMP     dMP   
dMP.aMP dMP    
VMMMP" dMMMMMP 
                                                                       """,
        """
   .aMMMb  dMP    .aMMBb  dMP dMP dMMMMb 
  dMP"VMP dMP    dMP"dMP dMP dMP dMP VMP 
 dMP     dMP    dMP dMP dMP dMP dMP dMP  
dMP.aMP dMP    dMP.aMP dMP.aMP dMP.aMP   
VMMMP" dMMMMMP VMMMP"  VMMMP" dMMMMP"    
                                         
                                  
         👾
                                                                       """,
        """
        
        
                                                     .aMMMb  dMP     dMP 
                                                    dMP"dMP dMP     amr  
                                                   dMMMMMP dMP     dMP   
                                                  dMP dMP dMP     dMP    
                                                 dMP dMP dMMMMMP dMP     
                                                                           
         👾🛸
       🎉
                                                                       """,
        """ 
        
       .aMMMb  dMP    .aMMMb  dMP dMP dMMMMb         .aMMMb  dMP     dMP 
      dMP"VMP dMP    dMP"dMP dMP dMP dMP VMP        dMP"dMP dMP     amr  
     dMP     dMP    dMP dMP dMP dMP dMP dMP        dMMMMMP dMP     dMP   
    dMP.aMP dMP    dMP.aMP dMP.aMP dMP.aMP        dMP dMP dMP     dMP    
    VMMMP" dMMMMMP VMMMP"  VMMMP" dMMMMP"        dMP dMP dMMMMMP dMP     
         👾
       🎉🛸
         🎊
                                                                       """
    ]

    for frame in devopsDance_frames:
        print(frame)
        time.sleep(0.5)  
        print("\033[H\033[J", end="")  

class CloudEngineer:
    def __init__(self):
        self.name = "Ali"
        self.role = "Aspiring Software Engineer 🚀"
        self.status = ["Kubernetes", "zOS & Cobol", "SpringBoot", "and cloud infrastructure"]
        self.languages_programming = ["Python", "Java", "Go"]
        self.languages_real = ["English", "Sarcasm_JK"]
        self.website = "https://cloudali.net"

    def static_final_frame(self):
        static_frame = """
       .aMMMb  dMP    .aMMMb  dMP dMP dMMMMb         .aMMMb  dMP     dMP 
      dMP"VMP dMP    dMP"dMP dMP dMP dMP VMP        dMP"dMP dMP     amr  
     dMP     dMP    dMP dMP dMP dMP dMP dMP        dMMMMMP dMP     dMP   
    dMP.aMP dMP    dMP.aMP dMP.aMP dMP.aMP        dMP dMP dMP     dMP    
    VMMMP" dMMMMMP VMMMP"  VMMMP" dMMMMP"        dMP dMP dMMMMMP dMP     
         🛸
         👾
           📡 🛸
                                                                       """
        print(static_frame)
        print("----- Docker Container Ready! Entering the matrix 👾 -----\n")

    def say_hi(self):
        self.static_final_frame()  
        print(f"Hey there ! My name is \033[35m{self.name}\033[0m, and I am an \033[35m{self.role}\033[0m.")
        print(f"I am currently learning everything about {', '.join(self.status)}.")
        print("I program primarily in {}, but also use {} from time to time.\n".format(
            self.languages_programming[0],
            ' & '.join(self.languages_programming[1:])
        ))
        print("Thanks for stopping in! I hope my profile and projects are more thrilling than your average cat video. Spoiler: they might not be!.\n")
        print(f"You can find more about me and my projects 👉 \033[35m{self.website}\033[0m 👈 [CMD/CTRL + CLICK].\n")  

    def start(self):
        welcome()
        self.say_hi()

if __name__ == "__main__":
    me = CloudEngineer()
    me.start()
