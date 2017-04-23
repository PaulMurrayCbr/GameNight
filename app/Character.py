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
            tmax += hp.max if hp.max else 0
            tcur += hp.current if hp.current else 0
            
    return { 'totalhp' :  (tmax, tcur), 'hps': hps, 'ablative': abl}
