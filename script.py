def jg_save_xyzrgb_plyfile(ply_file, np_points, removeBlackPoints=True):
    """ input : path to plyfile and numpy array of shape (N,6)"""
    points = []
    for p in np_points.tolist():
        if p[3]==0 and p[4]==0 and p[5]==0 and removeBlackPoints:
            # to remove black point
            pass
        else:
            points.append("%f %f %f %d %d %d 0\n"%tuple(p))
    f = open(ply_file,"w")
    f.write('''ply
format ascii 1.0
element vertex %d
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
property uchar alpha
end_header
%s
'''%(len(points),"".join(points)))
    f.close()
