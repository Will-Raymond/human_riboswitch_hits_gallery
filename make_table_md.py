# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:49:19 2023

@author: willi
"""

import pandas as pd
import os
import pickle
import numpy as np

md_dir = './_mds/'
display_dir = './'




def make_md2(gene, master_str_tuple, i):

    #<! ![](../../alns_9.28.22/%s?raw=true)>
    with open(md_dir + '%s.md'%gene,'w') as f:
       
        md_text = '''---
layout: page
title: "%s"
permalink: /_mds/%s/
exclude: true
---

<link rel="stylesheet" href="../../custom.css">


<div> Detected as RS by %s out of 20 classifiers </div>



<div class="row" >
  <div class="column">
    <a href="../../_mds/%s/"><img src="../../icons/arrow_left.png" alt="arrow left" style="width:100%%"></a>
  </div>
  <div class="column_center">
    <table>
      <tr>
        <th>%s</th>
        <th>%s - Similarity: %s</th>
        <th>%s - Similarity: %s</th>
        <th>%s - Similarity: %s</th>
      </tr>
        <tr>
            <td>
                    UTR: %s<br>
                    Gene: %s<br>
                    MFE: %s<br>
                    ENS: %s<br>
                    Length: %s<br>
                    Predicted Ligands:<br>
                    %s<br>
                    %s<br>
                    %s<br>         
            </td>
            <td>
                    RS: %s<br>
                    MFE: %s<br>
                    Ligand: %s<br>
                    %s<br>
            </td>
            <td>
                    RS: %s<br>
                    MFE: %s<br>
                    Ligand: %s<br>
                    %s<br>
            </td>
            <td>
                    RS: %s<br>
                    MFE: %s<br>
                    Ligand: %s<br>
                %s<br>
            </td>
        </tr>
      <tr>
        <td><img src="../../alns/dot/UTR_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/dot/RS_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/dot/RS_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/dot/RS_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
      </tr>
      <tr>
        <td><img src="../../alns/circ/circ_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/circ/circ_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/circ/circ_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/circ/circ_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
      </tr>
      <tr>
        <td></td>
        <td><img src="../../alns/feat/feat_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/feat/feat_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
        <td><img src="../../alns/feat/feat_%s_%s.png" alt="UTR-RS hit comparison" style="width:100%%"></td>
      </tr>
    </table>
    </div>
  <div class="column">
    <a href="../../_mds/%s/"><img src="../../icons/arrow_right.png" alt="arrow right" style="width:100%%"></a>
  </div>
</div>


<div class="row" >
    <div class="column_center">
        <img src="../../alns/feat/featcomp_%s.png" alt="UTR-RS hit comparison" style="width:100%%">
    </div>
</div>

<div class="row" >
    <div class="column_center">
        <img src="../../alns/bpp/bpp_%s.png" alt="UTR-RS hit comparison" style="width:100%%">
    </div>
</div>



<div class="row">
    <div class="column_center">
        <img src="../../alns/ens/ens_%s.png" alt="ML ensemble output for the 5prime UTR" style="width:100%%">
    </div>
</div>


**Information**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Link to the sequence source">Link</span> | -  | <a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>     |<a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>  | <a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>   |
| <span title="ID within respective databases">ID</span>  | %s     | %s     | %s     | %s     |
| <span title="Length of the sequence in question">Length</span>  | %s     |  %s    | %s   |  %s    |
| <span title="Similarity score calculated from all similarity metrics">Similarity</span>  | - | %s | %s | %s |
| <span title="Ensemble classification via all 19 ML classifiers">Ensemble Norm</span>  | %s | - | - | - |
| <span title="Nupack Mean Free Energy of the secondary structure">MFE</span>  | %s | %s | %s | %s |
| <span title="Reported Ligand match on RNAcentral or via RFAM">Ligands</span>  | - | %s | %s | %s |
| <span title="Homo Sapiens gene abbreviation">Gene</span>  | %s | - | - | - |
| <span title="Link to the sequence source">Downstream protein</span>  | <a href="https://www.genecards.org/cgi-bin/carddisp.pl?gene=%s" target="_blank" rel="noopener noreferrer"> Genecard </a>   |    -    | -  | - |


**Similarity metrics**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Structural feature squared error">Struct SE</span> | - | %s | %s | %s |
| <span title="Length difference squared error">Length SE</span> | - | %s | %s | %s |
| <span title="Edit distance of both dot structures">Lev Distance</span> | - | %s | %s | %s |
| <span title="Unbranched stack count">UBS</span>| %s | %s | %s | %s |
| <span title="Branched stack counts">BS</span> | %s | %s | %s | %s |
| <span title="Inner loop left count">ILL</span> | %s | %s | %s | %s |
| <span title="Inner loop right count">ILR</span> | %s | %s | %s | %s |
| <span title="Hairpin counts">H</span> | %s | %s | %s | %s |
| <span title="Bulges left count">BL</span> | %s | %s | %s | %s |
| <span title="Bulges right count">BR</span> | %s | %s | %s | %s |
| <span title="Unpaired nucleotide %%">UN</span> | %s | %s | %s | %s |

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


[Back to Ensemble of 20 Table](../../display_436)

[Back to Ensemble of 1 Table](../../display_1533)
'''%master_str_tuple
        f.writelines(md_text)
        






def make_md(gene, master_str_tuple):

    #<! ![](../../alns_9.28.22/%s?raw=true)>
    with open(md_dir + '%s.md'%gene,'w') as f:
       
        md_text = '''---
layout: page
title: "%s"
permalink: /_mds/%s/
exclude: true
---

<link rel="stylesheet" href="../../custom.css">


<div> Detected as RS by %s out of 20 classifiers </div>

<div class="row" >
  <div class="column">
    <a href="../../_mds/%s/"><img src="../../icons/arrow_left.png" alt="arrow left" style="width:100%%"></a>
  </div>
  <div class="column_center">
    <img src="../../alns_10.27.23/%s?raw=true" alt="UTR-RS hit comparison" style="width:100%%">
  </div>
  <div class="column">
    <a href="../../_mds/%s/"><img src="../../icons/arrow_right.png" alt="arrow right" style="width:100%%"></a>
  </div>
</div>




**Information**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Link to the sequence source">Link</span> | <a href="%s" target="_blank" rel="noopener noreferrer">UTRdb</a>   | <a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>     |<a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>  | <a href="%s" target="_blank" rel="noopener noreferrer">RNAcentral</a>   |
| <span title="ID within respective databases">ID</span>  | %s     | %s     | %s     | %s     |
| <span title="Length of the sequence in question">Length</span>  | %s     |  %s    | %s   |  %s    |
| <span title="Similarity score calculated from all similarity metrics">Similarity</span>  | - | %s | %s | %s |
| <span title="Ensemble classification via all 19 ML classifiers">Ensemble Norm</span>  | %s | - | - | - |
| <span title="Nupack Mean Free Energy of the secondary structure">MFE</span>  | %s | %s | %s | %s |
| <span title="Reported Ligand match on RNAcentral or via RFAM">Ligands</span>  | - | %s | %s | %s |
| <span title="Homo Sapiens gene abbreviation">Gene</span>  | %s | - | - | - |
| <span title="Link to the sequence source">Downstream protein</span>  | <a href="https://www.genecards.org/cgi-bin/carddisp.pl?gene=%s" target="_blank" rel="noopener noreferrer"> Genecard </a>   |    -    | -  | - |


**Similarity metrics**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Structural feature squared error">Struct SE</span> | - | %s | %s | %s |
| <span title="Length difference squared error">Length SE</span> | - | %s | %s | %s |
| <span title="Edit distance of both dot structures">Lev Distance</span> | - | %s | %s | %s |
| <span title="Unbranched stack count">UBS</span>| %s | %s | %s | %s |
| <span title="Branched stack counts">BS</span> | %s | %s | %s | %s |
| <span title="Inner loop left count">ILL</span> | %s | %s | %s | %s |
| <span title="Inner loop right count">ILR</span> | %s | %s | %s | %s |
| <span title="Hairpin counts">H</span> | %s | %s | %s | %s |
| <span title="Bulges left count">BL</span> | %s | %s | %s | %s |
| <span title="Bulges right count">BR</span> | %s | %s | %s | %s |
| <span title="Unpaired nucleotide %%">UN</span> | %s | %s | %s | %s |

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


[Back to Ensemble of 20 Table](../../display_436)

[Back to Ensemble of 1 Table](../../display_1533)
'''%master_str_tuple
        f.writelines(md_text)
        

def make_md_table(utr_list, genes, best_RSs, utr_probas, algn_scores, MFEs, norm_algn, classifier_count, table_name='display'):
    
    
    with open(display_dir + '%s.md'%table_name,'w') as f:
        
        
        x = '''
        ---
        layout: page
        title: "Ensemble of 1"
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
        <th> <div title="What gene is this transcript associated with?"> Gene </div></th>
        <th> <div title="ID in original UTRdb"> 5'UTR UTRdb 1.0 ID </div></th>
        <th> <div title="Defunct link to original UTRdb"> UTRdb 1.0 link </div></th>
        <th> <div title="ID on RNA central of closest RS match"> Closest RS ID</div></th>
        <th> <div title="Link to closest RS match on RNA central "> Closest RS link </div></th>
        <th> <div title="Average RS probability reported by the classifiers"> Ensemble Norm </div></th>
        <th> <div title="How many classifiers found this 5'UTR to be a RS?"> Ensemble Count </div></th>
        <th> <div title="Best similarity metric between 5'UTR hit and RS normalized(length distance + edit distance + structural feature vector MSE)/3"> Similarity </div></th>
        <th> <div title="Mean free energy of the NUPACK predicted dot structure"> MFE </div></th>
        <th><div title="Link to the visualization page of this hit"> Visualization </div></th>
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
            '<td>%.4f</td>\n'%utr_probability,
            '<td>%i</td>\n'%classifier_count[i],
            '<td>%.4f</td>\n'%algn_score,
            '<td>%.3f</td>\n'%MFE,
            '<td><a href="/human_riboswitch_hits_gallery/_mds/%s">=></a></td>\n'%gene,
            '</tr>\n',
            ]
            f.writelines(lines)
            
            
        f.write('</tbody>')
        f.write('</table>')
        
        



with open('./data_files/utr_probas.pkl', 'rb') as f:
    utr_probas = pickle.load(f)
    
ENS_count = np.load('./data_files/ENS_count.npy')
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


with open('./data_files/rs1_mfe.pkl', 'rb') as f:
    rs1_mfes = pickle.load(f)
with open('./data_files/rs2_mfe.pkl', 'rb') as f:
    rs2_mfes = pickle.load(f)
with open('./data_files/rs3_mfe.pkl', 'rb') as f:
    rs3_mfes = pickle.load(f)

with open('./data_files/rs1_desc.pkl', 'rb') as f:
    rs1_descs = pickle.load(f)
with open('./data_files/rs2_desc.pkl', 'rb') as f:
    rs2_descs = pickle.load(f)
with open('./data_files/rs3_desc.pkl', 'rb') as f:
    rs3_descs = pickle.load(f)

with open('./data_files/utr_ligands.pkl', 'rb') as f:
    utr_pls = pickle.load(f)

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



ens20 = False
if ens20 == True:
    ulist_keep = []
    keep_indexes = []
    for i in range(len(ulist)):
        if ENS_count[i] == 20:
            ulist_keep.append(ulist[i])
            keep_indexes.append(i)
    
            
    ulist2 = [ulist[i] for i in range(len(ulist)) if i in keep_indexes]
    utr_probas = [utr_probas[i] for i in range(len(ulist)) if i in keep_indexes]
    used_genes = [used_genes[i] for i in range(len(ulist)) if i in keep_indexes]
    best_RSs = [best_RSs[i] for i in range(len(ulist)) if i in keep_indexes]
    MFEs = [MFEs[i] for i in range(len(ulist)) if i in keep_indexes]
    fpaths = [fpaths[i] for i in range(len(ulist)) if i in keep_indexes]
    norm_algn = [norm_algn[i] for i in range(len(ulist)) if i in keep_indexes]
    algn_scores_1 = [algn_scores_1[i] for i in range(len(ulist)) if i in keep_indexes]
    algn_scores_2 = [algn_scores_2[i] for i in range(len(ulist)) if i in keep_indexes]
    algn_scores_3 = [algn_scores_3[i] for i in range(len(ulist)) if i in keep_indexes]
    
    rs1_ids = [rs1_ids[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_ids = [rs2_ids[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_ids = [rs3_ids[i] for i in range(len(ulist)) if i in keep_indexes]
    
    rs1_seqs = [rs1_seqs[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_seqs = [rs2_seqs[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_seqs = [rs3_seqs[i] for i in range(len(ulist)) if i in keep_indexes]
    utr_seqs = [utr_seqs[i] for i in range(len(ulist)) if i in keep_indexes]

    rs1_mfes = [rs1_mfes[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_mfes = [rs2_mfes[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_mfes = [rs3_mfes[i] for i in range(len(ulist)) if i in keep_indexes]
    utr_mfes = [utr_mfes[i] for i in range(len(ulist)) if i in keep_indexes]

    rs1_ligands = [rs1_ligands[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_ligands = [rs2_ligands[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_ligands = [rs3_ligands[i] for i in range(len(ulist)) if i in keep_indexes]

    rs1_length_MSE = [rs1_length_MSE[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_length_MSE = [rs2_length_MSE[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_length_MSE = [rs3_length_MSE[i] for i in range(len(ulist)) if i in keep_indexes]

    rs1_lev_dist = [rs1_lev_dist[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_lev_dist = [rs2_lev_dist[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_lev_dist = [rs3_lev_dist[i] for i in range(len(ulist)) if i in keep_indexes]

    rs1_struct_mse = [rs1_struct_mse[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_struct_mse = [rs2_struct_mse[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_struct_mse = [rs3_struct_mse[i] for i in range(len(ulist)) if i in keep_indexes]

    rs1_feats = [rs1_feats[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_feats = [rs2_feats[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_feats = [rs3_feats[i] for i in range(len(ulist)) if i in keep_indexes]
    utr_feats = [utr_feats[i] for i in range(len(ulist)) if i in keep_indexes]


    rs1_mfes = [rs1_mfes[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_mfes = [rs2_mfes[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_mfes = [rs3_mfes[i] for i in range(len(ulist)) if i in keep_indexes]    
    
    rs1_descs = [rs1_descs[i] for i in range(len(ulist)) if i in keep_indexes]
    rs2_descs = [rs2_descs[i] for i in range(len(ulist)) if i in keep_indexes]
    rs3_descs = [rs3_descs[i] for i in range(len(ulist)) if i in keep_indexes]   
    
    utr_pls = [utr_pls[i] for i in range(len(ulist)) if i in keep_indexes]    


utr_pls = utr_pls[::2]

sorted_genes = sorted(used_genes)

sort_proba = np.sort(utr_probas)[::-1]
sort_index = np.argsort(utr_probas)[::-1].tolist()
page_order = [used_genes[i] for i in sort_index]

'''
make_md_table(ulist, used_genes, best_RSs, utr_probas, algn_scores_1, MFEs, norm_algn, ENS_count, table_name='display_1533')  
'''

previously_used_indexes = []
for i in range(len(ulist)):
    print(used_genes[i])
    file = fpaths[i]
    gis = page_order.index(used_genes[i])
    if gis != 0:
        previous_file = page_order[gis-1]
    else:
        previous_file = page_order[gis]
    if gis != 1532:
        next_file = page_order[gis+1]
    else:
        next_file = page_order[gis]
    enscount = ENS_count[i]
        
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
    
    uniprot_link = protein
    
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
    
    rs1_mfe = rs1_mfes[i]
    rs2_mfe = rs2_mfes[i]
    rs3_mfe = rs3_mfes[i]
    
    rs1_desc = rs1_descs[i]
    rs2_desc = rs2_descs[i]
    rs3_desc = rs3_descs[i]    
    
    utr_pl = utr_pls[i]
    if len(utr_pl) == 1:
        utr_pl = [utr_pl[0] + ' - 20/20', '', '']

    if len(utr_pl) == 2:
        utr_pl = [utr_pl[0], utr_pl[1], '']

    if len(utr_pl) == 3:
        utr_pl = [utr_pl[0], utr_pl[1], utr_pl[2]]    

    utr_UBS, utr_BS, utr_ILL, utr_ILR, utr_H, utr_BL, utr_BR, utr_UN = utr_feats[i]
    rs1_UBS, rs1_BS, rs1_ILL, rs1_ILR, rs1_H, rs1_BL, rs1_BR, rs1_UN  = rs1_feats[i]
    rs2_UBS, rs2_BS, rs2_ILL, rs2_ILR, rs2_H, rs2_BL, rs2_BR, rs2_UN = rs2_feats[i]
    rs3_UBS, rs3_BS, rs3_ILL, rs3_ILR, rs3_H, rs3_BL, rs3_BR, rs3_UN = rs3_feats[i]


    
    '''
    mst = [gene.upper(), gene.upper(), enscount, previous_file, file, next_file, utr_link, rs1_link, rs2_link,
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
    
    '''    
    k = str(i)
    mst = [gene.upper(), gene.upper(), str(enscount), previous_file, utr_id, rs1_id, rs1_sim,
           rs2_id, rs2_sim, rs3_id, rs3_sim,
           
           
           utr_id, gene.upper(), utr_mfe, ens, utr_l, utr_pl[0], utr_pl[1], utr_pl[2],
           rs1_id, rs1_mfe, rs1_ligand, rs1_desc.replace('-\n',''),#text
           rs2_id, rs2_mfe, rs2_ligand, rs2_desc.replace('-\n',''),#text
           rs3_id, rs3_mfe, rs3_ligand, rs3_desc.replace('-\n',''),#text
           
           utr_id, k, rs1_id, k, rs2_id, k, rs3_id, k, # ss
           utr_id, k, rs1_id, k, rs2_id, k, rs3_id, k, # circ
           rs1_id, k, rs2_id, k, rs3_id, k, # feat
           next_file, k, k, k, #utr_link
           
          rs1_link, rs2_link,
                        rs3_link, utr_id, rs1_id, rs2_id, rs3_id, 
                        utr_l, rs1_l, rs2_l, rs3_l, '{:.3f}'.format(rs1_sim), '{:.3f}'.format(rs2_sim), '{:.3f}'.format(rs3_sim), ens,
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
    for j in range(len(mst)):
        if isinstance(mst[j],str):
            master_str_tuple.append(mst[j])
        else:
            ss = '{:.3f}'.format(mst[j])
            if ss[-2:] == '00':
                ss = ss[:-3]
            master_str_tuple.append(ss)
                        
    make_md2(gene, tuple(master_str_tuple), i)

'''
from PIL import Image
for f in os.listdir('./alns_10.27.23/'):
    img = Image.open('./alns_10.27.23/' + f)
    img.crop((460,330, 3480,2660)).save('./alns_10.27.23/' + f)
'''