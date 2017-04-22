import models

def buildInfo(pc):
    tmax = 0
    tcur = 0
    
    hps = []
    abl = []
    
    for hp in pc.hps:
        if(hp.ablative_only):
            abl.append(hp)
        else:
            hps.append(hp)
            tmax += hp.max
            tcur += hp.current
            
    return { 'totalhp' :  (tmax, tcur), 'hps': hps, 'ablative': abl}
