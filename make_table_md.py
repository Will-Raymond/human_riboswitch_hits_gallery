# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:49:19 2023

@author: willi
"""

import pandas as pd
import os
import pickle


md_dir = './_mds/'
display_dir = './'

def make_md(gene, master_str_tuple):

    
    with open(md_dir + '%s.md'%gene,'w') as f:
       
        md_text = '''---
layout: page
title: "%s"
permalink: /_mds/%s/
exclude: true
---



![](../../alns_9.28.22/%s?raw=true)


**Information**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| Link | <a href="%s" target="_blank" rel="noopener noreferrer">UTRdb</a>   | <a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>     |<a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>  | <a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>   |
| ID | %s     | %s     | %s     | %s     |
| Length | %s     |  %s    | %s   |  %s    |
| Similarity | - | %s | %s | %s |
| Ensemble Norm | %s | - | - | - |
| MFE | %s | %s | %s | %s |
| Ligands | - | %s | %s | %s |
| Gene | %s | - | - | - |
| Downstream protein | blank for now %s   |    -    | -  | - |


**Similarity metrics**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| Struct MSE | - | %s | %s | %s |
| Length MSE | - | %s | %s | %s |
| Lev Distance | - | %s | %s | %s |
| UBS| %s | %s | %s | %s |
| BS | %s | %s | %s | %s |
| ILL | %s | %s | %s | %s |
| ILR | %s | %s | %s | %s |
| H | %s | %s | %s | %s |
| BL | %s | %s | %s | %s |
| BR | %s | %s | %s | %s |
| UN | %s | %s | %s | %s |

**Sequences**


<div style="overflow-x:auto;">

<table>
<colgroup>
<col width="30%%" />
<col width="70%%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">UTR seq + 25 </td>
<td markdown="span"> %s </td>
</tr>
<tr>
<td markdown="span">UTR dot + 25  </td>
<td markdown="span"> %s
</td>
</tr>


<tr>
<td markdown="span">RS 1 seq </td>
<td markdown="span"> %s
</td>
</tr>


<tr>
<td markdown="span">RS 1 dot </td>
<td markdown="span"> %s
</td>
</tr>


<tr>
<td markdown="span">RS 2 seq </td>
<td markdown="span"> %s
</td>
</tr>


<tr>
<td markdown="span">RS 2 dot </td>
<td markdown="span"> %s
</td>
</tr>


<tr>
<td markdown="span">RS 3 seq </td>
<td markdown="span"> %s
</td>
</tr>


<tr>
<td markdown="span">RS 3 dot </td>
<td markdown="span"> %s
</td>
</tr>

</tbody>
</table>


</div>


[Back to Table](../../display)
'''%master_str_tuple
        f.writelines(md_text)
        

def make_md_table(utr_list, genes, best_RSs, utr_probas, algn_scores, MFEs, norm_algn):
    
    
    with open(display_dir + 'display.md','w') as f:
        
        
        x = '''
        ---
        layout: page
        title: "UTR visualization"
        permalink: /display/
        datatable: true
        ---
        
        
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jq-3.6.0/dt-1.11.3/datatables.min.css"/>
         
        <script type="text/javascript" src="https://cdn.datatables.net/v/dt/jq-3.6.0/dt-1.11.3/datatables.min.js"></script>
        
        
        
        <script>
        $(document).ready(function(){
            $('table.display').DataTable( {
                paging: true,
                stateSave: true,
                searching: true
            }
                );
        });
        </script>
        
        
        <table id="maintable" class="display">
        <thead>
        <tr>
        <th>Gene</th>
        <th>5'UTR mRNA</th>
        <th>UTRdb link</th>
        <th>Closest RS</th>
        <th>RS link</th>
        <th>Ensemble Norm</th>
        <th>Similarity</th>
        <th>MFE</th>
        <th>Visualization</th>
        </tr>
        </thead>
        <tbody>
        '''
        
        f.writelines(x)
        
        for i in range(len(utr_list)):
            
            UTR = utr_list[i]
            MFE = MFEs[i]
            utr_probability = utr_probas[i]
            algn_score = norm_algn[i]
            gene = genes[i]
            best_RS = best_RSs[i]
            
            
            best_RS_url = best_RS.replace('_','/')
            lines = [
            '<tr>\n',
            '<td>%s</td>\n'%gene,
            '<td>%s</td>\n'%UTR,
            '<td><a href="http://utrdb.ba.itb.cnr.it/getutr/%s/1">UTR</a></td>\n'%UTR,
            '<td>%s</td>\n'%best_RS,
            '<td><a href="https://rnacentral.org/rna/%s">RS</a></td>\n'%best_RS_url,
            '<td>%.3f</td>\n'%utr_probability,
            '<td>%.3f</td>\n'%algn_score,
            '<td>%.3f</td>\n'%MFE,
            '<td><a href="/human_riboswitch_hits_gallery/_mds/%s">=></a></td>\n'%gene,
            '</tr>\n',
            ]
            f.writelines(lines)
            
            
        f.write('</tbody>')
        f.write('</table>')
        
        

with open('./data_files/utr_probas.pkl', 'rb') as f:
    utr_probas = pickle.load(f)
with open('./data_files/ulist.pkl', 'rb') as f:
    ulist = pickle.load(f)
with open('./data_files/genes.pkl', 'rb') as f:
    genes = pickle.load(f)
with open('./data_files/best_RSs.pkl', 'rb') as f:
    best_RSs = pickle.load(f)

with open('./data_files/MFEs.pkl', 'rb') as f:
    MFEs = pickle.load(f)
with open('./data_files/fpaths.pkl', 'rb') as f:
    fpaths = pickle.load(f)
with open('./data_files/norm_algn.pkl', 'rb') as f:
    norm_algn = pickle.load(f)
    
with open('./data_files/algn_scores_1.pkl', 'rb') as f:
    algn_scores_1 = pickle.load(f)
with open('./data_files/algn_scores_2.pkl', 'rb') as f:
    algn_scores_2 = pickle.load(f)
with open('./data_files/algn_scores_3.pkl', 'rb') as f:
    algn_scores_3 = pickle.load(f)
    
with open('./data_files/rs1_ids.pkl', 'rb') as f:
    rs1_ids = pickle.load(f)
with open('./data_files/rs2_ids.pkl', 'rb') as f:
    rs2_ids = pickle.load(f)
with open('./data_files/rs3_ids.pkl', 'rb') as f:
    rs3_ids = pickle.load(f)
    
with open('./data_files/rs1_seqs.pkl', 'rb') as f:
    rs1_seqs = pickle.load(f)
with open('./data_files/rs2_seqs.pkl', 'rb') as f:
    rs2_seqs = pickle.load(f)
with open('./data_files/rs3_seqs.pkl', 'rb') as f:
    rs3_seqs = pickle.load(f)
with open('./data_files/utr_seqs_l.pkl', 'rb') as f:
    utr_seqs = pickle.load(f)    


with open('./data_files/rs1_dots.pkl', 'rb') as f:
    rs1_dots = pickle.load(f)
with open('./data_files/rs2_dots.pkl', 'rb') as f:
    rs2_dots = pickle.load(f)
with open('./data_files/rs3_dots.pkl', 'rb') as f:
    rs3_dots = pickle.load(f)
with open('./data_files/utr_dots_l.pkl', 'rb') as f:
    utr_dots = pickle.load(f)    

with open('./data_files/rs1_MFEs.pkl', 'rb') as f:
    rs1_mfes = pickle.load(f)
with open('./data_files/rs2_MFEs.pkl', 'rb') as f:
    rs2_mfes = pickle.load(f)
with open('./data_files/rs3_MFEs.pkl', 'rb') as f:
    rs3_mfes = pickle.load(f)
with open('./data_files/MFEs.pkl', 'rb') as f:
    utr_mfes = pickle.load(f)    
    
with open('./data_files/rs1_ligands.pkl', 'rb') as f:
    rs1_ligands = pickle.load(f)
with open('./data_files/rs2_ligands.pkl', 'rb') as f:
    rs2_ligands = pickle.load(f)
with open('./data_files/rs3_ligands.pkl', 'rb') as f:
    rs3_ligands = pickle.load(f)
    
with open('./data_files/rs1_length_MSE.pkl', 'rb') as f:
    rs1_length_MSE = pickle.load(f)
with open('./data_files/rs2_length_MSE.pkl', 'rb') as f:
    rs2_length_MSE = pickle.load(f)
with open('./data_files/rs3_length_MSE.pkl', 'rb') as f:
    rs3_length_MSE = pickle.load(f)

with open('./data_files/rs1_lev_dist.pkl', 'rb') as f:
    rs1_lev_dist = pickle.load(f)
with open('./data_files/rs2_lev_dist.pkl', 'rb') as f:
    rs2_lev_dist = pickle.load(f)
with open('./data_files/rs3_lev_dist.pkl', 'rb') as f:
    rs3_lev_dist = pickle.load(f)

with open('./data_files/rs1_struct_mse.pkl', 'rb') as f:
    rs1_struct_mse = pickle.load(f)
with open('./data_files/rs2_struct_mse.pkl', 'rb') as f:
    rs2_struct_mse = pickle.load(f)
with open('./data_files/rs3_struct_mse.pkl', 'rb') as f:
    rs3_struct_mse = pickle.load(f)

with open('./data_files/rs1_feats.pkl', 'rb') as f:
    rs1_feats = pickle.load(f)
with open('./data_files/rs2_feats.pkl', 'rb') as f:
    rs2_feats = pickle.load(f)
with open('./data_files/rs3_feats.pkl', 'rb') as f:
    rs3_feats = pickle.load(f)
with open('./data_files/utr_feats.pkl', 'rb') as f:
    utr_feats = pickle.load(f)    

used_genes = []

for i in range(len(ulist)):
    gene = genes[i] 
    if gene not in used_genes:
        used_genes.append(gene)
    else:
        k = 0
        while gene in used_genes:
            if k == 0:
                gene = gene + '_' + str(k)
                k+=1
            else:
                gene = gene[:-1] + str(k)
                k+=1
       
        used_genes.append(gene)




#make_md_table(ulist, used_genes, best_RSs, utr_probas, algn_scores_1, MFEs, norm_algn)  

for i in range(len(ulist)):
    
    
    file = fpaths[i]
    gene = used_genes[i]
    utr_id = ulist[i]
    protein = genes[i]
    
    rs1_id = rs1_ids[i]
    rs2_id = rs2_ids[i]
    rs3_id = rs3_ids[i]
    
    rs1_link = "https://rnacentral.org/rna/%s"%rs1_id.replace('_','/')
    rs2_link = "https://rnacentral.org/rna/%s"%rs2_id.replace('_','/')
    rs3_link = "https://rnacentral.org/rna/%s"%rs3_id.replace('_','/')
    utr_link = "http://utrdb.ba.itb.cnr.it/getutr/%s/1"%utr_id
    
    uniprot_link = ''
    
    utr_seq = utr_seqs[i]
    rs1_seq = rs1_seqs[i]
    rs2_seq = rs2_seqs[i]
    rs3_seq = rs3_seqs[i]

    utr_dot = utr_dots[i]
    rs1_dot = rs1_dots[i]
    rs2_dot = rs2_dots[i]
    rs3_dot = rs3_dots[i]
    
    utr_l = len(utr_seq)
    rs1_l = len(rs1_seq)
    rs2_l = len(rs2_seq)
    rs3_l = len(rs3_seq)

    rs1_sim = algn_scores_1[i]
    rs2_sim = algn_scores_2[i]
    rs3_sim = algn_scores_3[i]
    ens = norm_algn[i]

    utr_mfe = utr_mfes[i]
    rs1_mfe = rs1_mfes[i]
    rs2_mfe = rs2_mfes[i]
    rs3_mfe = rs3_mfes[i]

    rs1_ligand = rs1_ligands[i]
    rs2_ligand = rs2_ligands[i]
    rs3_ligand = rs3_ligands[i]

    rs1_lmse = rs1_length_MSE[i]
    rs2_lmse = rs2_length_MSE[i]
    rs3_lmse = rs3_length_MSE[i]
    
    rs1_lev = rs1_lev_dist[i]
    rs2_lev = rs2_lev_dist[i]
    rs3_lev = rs3_lev_dist[i]
    
    rs1_mse = rs1_struct_mse[i]
    rs2_mse = rs2_struct_mse[i]
    rs3_mse = rs3_struct_mse[i]
    

    utr_UBS, utr_BS, utr_ILL, utr_ILR, utr_H, utr_BL, utr_BR, utr_UN = utr_feats[i]
    rs1_UBS, rs1_BS, rs1_ILL, rs1_ILR, rs1_H, rs1_BL, rs1_BR, rs1_UN  = rs1_feats[i]
    rs2_UBS, rs2_BS, rs2_ILL, rs2_ILR, rs2_H, rs2_BL, rs2_BR, rs2_UN = rs2_feats[i]
    rs3_UBS, rs3_BS, rs3_ILL, rs3_ILR, rs3_H, rs3_BL, rs3_BR, rs3_UN = rs3_feats[i]


    
    
    mst = [gene.upper(), gene.upper(), file, utr_link, rs1_link, rs2_link,
                        rs3_link, utr_id, rs1_id, rs2_id, rs3_id, 
                        utr_l, rs1_l, rs2_l, rs3_l, rs1_sim, rs2_sim, rs3_sim, ens,
                        utr_mfe, rs1_mfe, rs2_mfe, rs3_mfe,
                        rs1_ligand, rs2_ligand, rs3_ligand,
                        protein, uniprot_link,
                        rs1_lmse, rs2_lmse, rs3_lmse, 
                        rs1_lev, rs2_lev, rs3_lev,
                        rs1_mse, rs2_mse, rs3_mse,
                        utr_UBS, rs1_UBS, rs2_UBS, rs3_UBS,
                        utr_BS, rs1_BS, rs2_BS, rs3_BS,
                        utr_ILL, rs1_ILL, rs2_ILL, rs3_ILL,
                        utr_ILR, rs1_ILR, rs2_ILR, rs3_ILR,
                        utr_H, rs1_H, rs2_H, rs3_H,
                        utr_BL, rs1_BL, rs2_BL, rs3_BL,
                        utr_BR, rs1_BR, rs2_BR, rs3_BR,
                        utr_UN, rs1_UN, rs2_UN, rs3_UN, utr_seq, utr_dot,
                        rs1_seq, rs1_dot, rs2_seq, rs2_dot, rs3_seq, rs3_dot]
    
    master_str_tuple = []
    for i in range(len(mst)):
        if isinstance(mst[i],str):
            master_str_tuple.append(mst[i])
        else:
            ss = '{:.2f}'.format(mst[i])
            if ss[-2:] == '00':
                ss = ss[:-3]
            master_str_tuple.append(ss)
                        
    make_md(gene, tuple(master_str_tuple))
