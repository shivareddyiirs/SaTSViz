##This file contains the function which reads the output of SaTScan analysis and creates two shapefiles , depending on the result, for visualization.

##Import required files
import shapefile
def make_shape(path,file_name):
    fout=open(path+'/'+ file_name+'.out.gis.txt','r')
    fo=open(path+'/'+ file_name+'.out.col.txt','r')
    fout1=open(path+'/'+ file_name+'.geo','r')

    t=[]
    g=[]
    c=[]
    l=0
    m=0
    n=0
   
## Read .out.gis.txt file and put it in a list
    while True:
        testline = fout.readline()
        t.append(testline.split())
        if len(testline) ==0 :
            break
        l=l+1

## Read .out.col.txt file and put it in a list
    while True:
        col_line = fo.readline()
        c.append(col_line.split())
        if len(col_line) ==0 :
            break
        n=n+1

		
## Read .geo.txt file and put it in a list        
    while True:
        geoline = fout1.readline()
        g.append(geoline.split())
        if len(geoline) ==0 :
            break
        m=m+1


## seek bakc to the start of the files
    fout.seek(0)
    fo.seek(0)
    fout1.seek(0)
    
## Open a shapefile for writing, define its type (point or polygon) and define its fields
    w=shapefile.Writer(shapefile.POINT)
    w.autoBalance =1
    w.shapeType=1
    w.field('Cname')
    w.field('Cid')
    w.field('p-value','F')
    w.field('X','F')
    w.field('Y','F')

## Write the shapefile - filename_cluster.shp
    for i in range(l):
       for j in range(m):
           if t[i][0]== g[j][0]:
               w.point(float(g[j][1]),float(g[j][2]))
               w.record(t[i][0],t[i][1],t[i][2],g[j][1],g[j][2])

##Save the shapefile			   
    w.save(path+'/'+file_name+'_cluster')


##do the same to write another shapefile - filename_col_cluster.shp
    wr=shapefile.Writer(shapefile.POINT)
    wr.autoBalance =1
    wr.shapeType=1
    wr.field('Cid')
    wr.field('C_start')
    wr.field('X','F')
    wr.field('Y','F')
    wr.field('radius','F')
    wr.field('#points','F')
    wr.field('p-value','F')
    wr.field('#cases','F')

    for j in range(n):
        wr.point(float(c[j][2]),float(c[j][3]))
        wr.record(c[j][0],c[j][1],c[j][2],c[j][3],c[j][4],c[j][7],c[j][9],c[j][10])

    wr.save(path+'/' + file_name + '_col_cluster')   

    fout.close()
    fo.close()
    fout1.close()

