#Copying files in Winamp playlist
    import sys
    import shutil
    import os
    def main():
        if(len(sys.argv)!=3):
            print "USAGE-cd to script location and type- python ",sys.argv[0]," <path to m3u file>"," <path to destination>"
            sys.exit()
        playlist=sys.argv[1]
        dest=sys.argv[2]
        f=open(playlist)
        #raw=f.read()
        if not os.path.exists(playlist):
            print "path to m3u file doesn't exist.. try again"
            sys.exit()
        if not os.path.exists(dest):
            print "dest path doesn't exist..creating.."
            os.makedirs(dest)
            print "path created"
        for line in f.readlines():
            if line[0]!='#':
                fline=line[:-1] 
                fname=os.path.split(fline)[-1]
                shutil.copyfile(fline,dest+"//"+fname)
                print line+" DONE"
                
        
        
        
        
    if __name__ == '__main__':
    	main()
