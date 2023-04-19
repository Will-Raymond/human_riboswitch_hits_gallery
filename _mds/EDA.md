---
layout: page
title: "EDA"
permalink: /_mds/EDA/
exclude: true
---

<link rel="stylesheet" href="../../custom.css">


<div> Detected as RS by 4 out of 20 classifiers </div>

<div class="row" >
  <div class="column">
    <a href="../../_mds/RNF125/"><img src="../../icons/arrow_left.png" alt="arrow left" style="width:100%"></a>
  </div>
  <div class="column_center">
    <img src="../../alns_9.28.22/aln_5HSAA033225_0.828.png?raw=true" alt="UTR-RS hit comparison" style="width:100%">
  </div>
  <div class="column">
    <a href="../../_mds/HDGF/"><img src="../../icons/arrow_right.png" alt="arrow right" style="width:100%"></a>
  </div>
</div>




**Information**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Link to the sequence source">Link</span> | <a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033225/1" target="_blank" rel="noopener noreferrer">UTRdb</a>   | <a href="https://rnacentral.org/rna/URS000231FE77/682795" target="_blank" rel="noopener noreferrer">RNAcentral</a>     |<a href="https://rnacentral.org/rna/URS0000AB8329/266117" target="_blank" rel="noopener noreferrer">RNAcentral</a>  | <a href="https://rnacentral.org/rna/URS00023255C8/411922" target="_blank" rel="noopener noreferrer">RNAcentral</a>   |
| <span title="ID within respective databases">ID</span>  | 5HSAA033225     | URS000231FE77_682795     | URS0000AB8329_266117     | URS00023255C8_411922     |
| <span title="Length of the sequence in question">Length</span>  | 172     |  171    | 170   |  172    |
| <span title="Similarity score calculated from all similarity metrics">Similarity</span>  | - | 0.94 | 0.92 | 0.94 |
| <span title="Ensemble classification via all 19 ML classifiers">Ensemble Norm</span>  | 0.94 | - | - | - |
| <span title="Nupack Mean Free Energy of the secondary structure">MFE</span>  | -48.17 | -49.07 | -86.19 | -52.66 |
| <span title="Reported Ligand match on RNAcentral or via RFAM">Ligands</span>  | - | cobalamin | cobalamin | cobalamin |
| <span title="Homo Sapiens gene abbreviation">Gene</span>  | EDA | - | - | - |
| <span title="Link to the sequence source">Downstream protein</span>  | <a href="https://www.genecards.org/cgi-bin/carddisp.pl?gene=EDA" target="_blank" rel="noopener noreferrer"> Genecard </a>   |    -    | -  | - |


**Similarity metrics**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Structural feature squared error">Struct SE</span> | - | 4 | 40 | 20 |
| <span title="Length difference squared error">Length SE</span> | - | 1 | 4 | 0 |
| <span title="Edit distance of both dot structures">Lev Distance</span> | - | 54 | 56 | 57 |
| <span title="Unbranched stack count">UBS</span>| 12 | 12 | 14 | 14 |
| <span title="Branched stack counts">BS</span> | 0 | 0 | 0 | 0 |
| <span title="Inner loop left count">ILL</span> | 1 | 2 | 1 | 3 |
| <span title="Inner loop right count">ILR</span> | 4 | 3 | 3 | 3 |
| <span title="Hairpin counts">H</span> | 6 | 6 | 5 | 5 |
| <span title="Bulges left count">BL</span> | 2 | 3 | 7 | 5 |
| <span title="Bulges right count">BR</span> | 2 | 3 | 5 | 3 |
| <span title="Unpaired nucleotide %">UN</span> | 0.11 | 0.16 | 0.13 | 0.08 |

**Sequences**


<div style="overflow-x:auto;">

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
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
<td markdown="span"> aacuagauagaccauuaguguauccagaguugacauuaccuguguuaaggcucuucgaucaagaacauaacuaggaaucauucgaggugauucaaggccuguuuuccucaggucuugcuaagccugugaccugucagcuaugcuuagATGGGCTACCCGGAGGTGGAGCGCA </td>
</tr>
<tr>
<td markdown="span">UTR dot + 25  </td>
<td markdown="span"> .....((((.((.....)).))))..((((((((((.....))))))..))))(((......))).........((((((((...))))))))((((((((.......))))))))(((..(((((((.(((((((((...)))..)))))).)))....))))..)))...
</td>
</tr>


<tr>
<td markdown="span">RS 1 seq </td>
<td markdown="span"> GGUAUAACUCGGAUAUCUGGUGUUCGGGAAGACGGUGCAAAUCCGUCACUACCGCGUAACUGUAAGCGCUAAGAGCCUGGCAUAUAAGGUCACUGGGAUCAGAGUCCUGGGAAGGCCGAUCAAGCUCCACGAGGCGCAAGUCAGGAGACCGGCCAGAUACGGGCUUAAUUC
</td>
</tr>


<tr>
<td markdown="span">RS 1 dot </td>
<td markdown="span"> .......(((((((((...)))))))))..(((((.......)))))......((((........)))).....((((........))))..(((((((....))))))).(((.((((((..(((.(.(..(((....)))..).)...)))..))).))).))).....
</td>
</tr>


<tr>
<td markdown="span">RS 2 seq </td>
<td markdown="span"> AAGGGAAUCCGGUGAGAAUCCGGAGCGGUCCCGCCACUGUGAGCGGCGAGGCCGGUCCCGCCUUUUGAGGGGGCUCCUCCCGGGAGGGGUCCCGGUCACUGGGCCACCGCCAGAGCGGGGCCCGGGAAGGCCGCGGAGCCGCGCCGCCCGAGCCGCGAGCCAGGAGACCU
</td>
</tr>


<tr>
<td markdown="span">RS 2 dot </td>
<td markdown="span"> ...(((.((......)).)))(((.(((((.((((.((...)).)))).))))).))).......(((.((((((((((....))))))))))..)))(((((((.((((....)))))))))))...((((((((..(.((...))..)..))))).))).........
</td>
</tr>


<tr>
<td markdown="span">RS 3 seq </td>
<td markdown="span"> UGAUAGUGUAAGGGAAUGGGUGCUUUGUGCUUAAUAGGGAAGUCCGGUGUAAUACCGGCACGGUCCCGCCACUGUAAUGGGGAUGCUUCCUAAAUUUGCCACUGGGAAACCGGGAAGGCUUAGGGCGGCGAUGAACCAGAGUCAGGAGACCUGCCUGUUCUAACACACGCCG
</td>
</tr>


<tr>
<td markdown="span">RS 3 dot </td>
<td markdown="span"> ....(((((((((.(.....).))))))))).....(((..((((((((...)))))).))..)))(.(((......))).).....((((((....(((.((((....))))...)))))))))(((((.((....((((.((((.......))))))))....)))))))
</td>
</tr>

</tbody>
</table>


</div>


[Back to Table](../../display)
