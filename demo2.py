
def cmd_and_para(cmd):
    gp = cmd.split(' ')
    gp_r = []
    gp_r.append(gp[0])

    para = ''
    # for i in range(1,len(gp)):
    #     if gp[i] != '':
    #         if not para:
    #             para = gp[i]
    #         else:
    #             para += ' ' + gp[i]
    for g in gp[1:]:
        if g != '':
            if not para:
                para = g
            else:
                para += ' ' + g

    if not para:
        return gp_r

    gp_r.append(para)
    return gp_r

if __name__ == '__main__':
    g_cmd = ''
    while g_cmd != 'exit':
        g_cmd = raw_input('>')

        gp = cmd_and_para(g_cmd)

        for g in gp:
            print g
