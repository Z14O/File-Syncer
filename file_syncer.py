import os
import time
import shutil
 
class file_syncer():
    def __init__(self,path1,path2):
        self.path1=path1
        self.path2=path2


    def os_file_list(self,path_of_the_folder_to_sync):#the outpu will be recived in two varaibles the first one in the folder paths list and the second part is the file paths list
        global folderpaths_of_client
        global filepaths_of_client

        folderpaths_of_client=list()
        filepaths_of_client=list()

    #this will walk through all the folders and subfolders to gather the file paths
        for folders,subfolders,files in os.walk(path_of_the_folder_to_sync):#Make a fuction for path!
                folderpaths_of_client.append(folders[len(path_of_the_folder_to_sync):])


                for file in files:
                    filepaths_of_client.append(folders[len(path_of_the_folder_to_sync):]+"\\"+file)
        folderpaths_of_client.sort()
        filepaths_of_client.sort()           
        return folderpaths_of_client,filepaths_of_client

    def run_sync(self):
        while True:

            self.listfol_from_path_1=list()
            self.listfol_from_path_2=list()
            self.listfil_from_path_1=list()
            self.listfil_from_path_2=list()
            self.listdel_from_path_1=list()
            self.listdel_from_path_2=list()


    
            self.listfol_from_path_1,self.listfil_from_path_1=self.os_file_list(self.path1)
            self.listfol_from_path_2,self.listfil_from_path_2=self.os_file_list(self.path2)

            
    
            for item in self.listfol_from_path_1:
                if item not in self.listfol_from_path_2:
                    
                    os.mkdir(self.path2+"\\"+item)
            for item in self.listfol_from_path_2:
                if item not in self.listfol_from_path_1:
                    os.mkdir(self.path1+'\\'+item)
    
    
            for item in self.listfil_from_path_1:
                if item not in self.listfil_from_path_2:
                    try:
                        shutil.copy2(self.path1+'\\'+item,self.path2+'\\'+item)
    
                    except:
                        pass
            
                    
                    
            for item in self.listfil_from_path_2:
                if item not in self.listfil_from_path_1:
                    try:
                        shutil.copy2(self.path2+'\\'+item,self.path1+'\\'+item)
    
                    except:
                        pass
            

            self.listfol_from_path_1,self.listfil_from_path_1=self.os_file_list(self.path1)
            self.listfol_from_path_2,self.listfil_from_path_2=self.os_file_list(self.path2)

            self.listdel_from_path_1=self.listfil_from_path_1
            self.listdel_from_path_2=self.listfil_from_path_2

            #Part to save the mtime log.       


            while True:
                time.sleep(0.5)

                

                self.listfil_from_path_1=list()
                self.listfil_from_path_2=list()

                self.listfol_from_path_1,self.listfil_from_path_1=self.os_file_list(self.path1)
                self.listfol_from_path_2,self.listfil_from_path_2=self.os_file_list(self.path2)
                test_val=0

                if self.listdel_from_path_1!= self.listfil_from_path_1:
                    test_val+=1

                    for item in self.listdel_from_path_1:
                        if item not in self.listfil_from_path_1:
                            try:
                                os.remove(self.path2+'\\'+item)
                            except:
                                pass
                        
                
                if self.listdel_from_path_2!= self.listfil_from_path_2:
                    test_val+=1

                    for item in self.listdel_from_path_2:
                        if item not in self.listfil_from_path_1:
                            try:
                                os.remove(self.path1+'\\'+item)
                            except:
                                pass


                if test_val!=0 :
                    break




                self.listmti_from_path_1=list()
                self.listmti_from_path_2=list()


                self.listfol_from_path_1,self.listfil_from_path_1=self.os_file_list(self.path1)

                #Note:We can use sets and continue in the future to make sure that even if someone added a new file it still won't bug the code.

                for item in self.listfil_from_path_1:
                    if item =='\n' or item =='':
                        continue
                    try:
                        item_temp1=os.path.getmtime(self.path1+'\\'+item)
                        item_temp2=os.path.getmtime(self.path2+'\\'+item)
                    except:
                        break
                    
                    if item_temp1!=item_temp2:
                        if item_temp1>item_temp2:
                            try:
                                os.remove(self.path2+'\\'+item)
                            except:
                                pass
                            
                            try:
                                shutil.copy2(self.path1+'\\'+item,self.path2+'\\'+item)
                            except:
                                break
                            
                        if item_temp1<item_temp2:
                            try:
                                os.remove(self.path1+'\\'+item)
                            except:
                                pass
                            
                            try:
                                shutil.copy2(self.path2+'\\'+item,self.path1+'\\'+item)
                            except:
                                break
                
        
                  





