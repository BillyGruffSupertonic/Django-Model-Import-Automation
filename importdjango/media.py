
from genericpath import exists
import time
import os 
import subprocess

def runchecks():

   
        # check os directory exists 
    if not os.path.exists('/mnt/chromeos/GoogleDrive'):
        print('Google Drive not mounted')

        exit()
        
    else:
        print('Google Drive mounted')
   

        if not os.path.exists(backupdir):
            print('Google Drive/MyDrive/cocb not found')
    
            exit()
        else:
            print('Google Drive/MyDrive/cocb found')
            # get contents of directory
            dir_contents = os.listdir(backupdir)
            print (dir_contents)
            # if there are no files in the directory    
            if len(dir_contents) == 0:
                print('No files in directory')
                print('ready to go')
       
            else:
                print('Files in directory, must remove first')
                if os.path.exists(maydir):
                    print('May directory found')
                    print('Running tar command')
                    # tar everything in cocb directory with get)time()
                    tar_command = 'tar cvfz ' + maydir + '/' + get_time() + '.tar.gz ' + backupdir
                    print(tar_command)
                    os.system(tar_command)

                    # tar check contents of file 
                    tar_contents = os.listdir(maydir)
                    print(tar_contents, "tar contents")



                    # remove all in backup directory
                    remove_command = 'rm -r ' + backupdir + "/*"
                    print('removed all files in backup directory')
                    print('ready to go')
                   
      

                else:
                    print('May directory not found')
                    exit()
            

                # # run tar command 
              
    

    return


def get_time():
    # get current time
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    print(current_time)
    


    return current_time





if __name__ == '__main__':
    backupdir = '/mnt/chromeos/GoogleDrive/MyDrive/cocb'
    maydir = '/mnt/chromeos/GoogleDrive/MyDrive/May'
    # make sure sudo 
    if os.geteuid() != 0:
        print('You must be root to run this script')
        exit()
    initialized = runchecks()






