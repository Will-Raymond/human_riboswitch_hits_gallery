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

def make_md(utr_id, gene, file):
    
    with open(md_dir + '%s.md'%gene,'w') as f:
        f.write('---\n')
        f.write('layout: page\n')
        f.write('title: "%s"\n'%gene.upper())
        f.write('permalink: /_mds/%s/\n'%gene.upper())
        f.write('---\n')
        f.write('\n')
        f.write('![](../../alns_9.28.22/%s?raw=true\n)'%file)
        f.write('\n')
        f.write('[Back to Table](../../display)\n')




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
        
        

with open('./utr_probas.pkl', 'rb') as f:
    utr_probas = pickle.load(f)
with open('./ulist.pkl', 'rb') as f:
    ulist = pickle.load(f)
with open('./genes.pkl', 'rb') as f:
    genes = pickle.load(f)
with open('./best_RSs.pkl', 'rb') as f:
    best_RSs = pickle.load(f)
with open('./algn_scores.pkl', 'rb') as f:
    algn_scores = pickle.load(f)
with open('./MFEs.pkl', 'rb') as f:
    MFEs = pickle.load(f)
with open('./fpaths.pkl', 'rb') as f:
    fpaths = pickle.load(f)
with open('./norm_algn.pkl', 'rb') as f:
    norm_algn = pickle.load(f)
    
#make_md_table(ulist, genes, best_RSs, utr_probas, algn_scores, MFEs, norm_algn)

for i in range(len(ulist)):
    make_md(ulist[i], genes[i], fpaths[i])    

