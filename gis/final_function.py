## This file contains the fucntion that reads the input shapefile and creates four files, .cas .pop .ctl .geo files, to be passed to SaTScan for analysis.

## Import required file
import shapefile
import os
import shutil

## Arguments are:
##arg1--> full path of the input shapefile
##arg2--> field chosen to be the Location Id
##arg3--> field chosen to be either case, control or population attribute
##arg4--> type of file to be made (.cas, .pop, .ctl)
##arg5--> Date field of the shapefile (if no date is there, NONE is selected)

def reading(arg1,arg2,arg3,arg4,arg5):

## Isolate file path and file name
    path=arg1
    path=path.split('/')
    fname=path.pop()
    path='/'.join(path)[0:]
    

    fname=fname.split('.')
    fname.reverse()
    file_name=fname.pop()
    
## Read the shapefile
    read = shapefile.Reader(arg1)
    file_fields=read.fields
    pts=read.shapes()
    date='NONE'
    p_or_c='NONE'
    
## Get index of the chosedn fields
    l1=len(file_fields)
    field_names=list(file_fields)
    for i in range(l1):
        field_names[i]=file_fields[i][0]

    v1= field_names.index(arg2)-1
    if arg3!=p_or_c:
        v2= field_names.index(arg3)-1

    if arg5 != date:
        v3=field_names.index(arg5)-1
        
##Read all records of shapefile and create empty lists
    rec = read.records()
    l=len(rec)
    rec1=list(rec)
    rec2=list(rec)
    rec3=list(rec)
    geo1=list(pts)

##Re-assign all the coordinates of the shapefile to a list
    for i in range(l):
        j=0
        geo1[i]=pts[i].points[j]
        j=j+1
        
    
    
    if arg4 == 'case' or arg4 == 'CASE':
        calling_obj='cas'
    elif arg4 == 'population' or arg4 == 'POPULATION':
        calling_obj='pop'
    elif arg4 == 'control'or arg4 == 'CONTROL' :
        calling_obj='ctl'

## Write file using the chosen fields		
    if arg3== p_or_c:
        pass
    else:
        fout = open(path+'\\' +file_name+'.'+ calling_obj,'w')        
        if arg5 == date :
            for i in range(l):
                rec1[i]=rec[i][v1]
                rec2[i]=rec[i][v2]
                fout.write(str(rec1[i])+'\t'+ str(rec2[i])+'\n')
            fout.close()
                
        elif arg5!= date and calling_obj == 'cas':
            for i in range(l):
                rec1[i]=rec[i][v1]
                rec2[i]=rec[i][v2]
                rec3[i]=rec[i][v3]
                fout.write(str(rec1[i])+'\t'+ str(rec2[i])+'\t'+ str(rec3[i])+'\n')
            fout.close()
            
	elif arg5!=date:
            if calling_obj == 'pop' or calling_obj == 'ctl':
                for i in range(l):
                    rec1[i]=rec[i][v1]
                    rec2[i]=rec[i][v2]
                    fout.write(str(rec1[i])+'\t'+ str(rec2[i])+'\n')
            fout.close()
                
## Write file with all the coordinates
    fout1 = open(path+'\\'+file_name+ '.geo','w')
    for i in range(l):
        fout1.write(str(rec1[i])+'\t'+ str(geo1[i][0])+'\t'+ str(geo1[i][1])+'\n')
    fout1.close()


 
    

    
    
