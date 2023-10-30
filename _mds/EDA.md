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
    <img src="../../alns_10.27.23/aln_5HSAA033225_0.828.png?raw=true" alt="UTR-RS hit comparison" style="width:100%">
  </div>
  <div class="column">
    <a href="../../_mds/HDGF/"><img src="../../icons/arrow_right.png" alt="arrow right" style="width:100%"></a>
  </div>
</div>




**Information**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Link to the sequence source">Link</span> | <a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033225/1" target="_blank" rel="noopener noreferrer">UTRdb</a>   | <a href="https://rnacentral.org/rna/URS000231FE77/682795" target="_blank" rel="noopener noreferrer">RNAcentral</a>     |<a href="https://rnacentral.org/rna/URS0000E23FFC/1339248" target="_blank" rel="noopener noreferrer">RNAcentral</a>  | <a href="https://rnacentral.org/rna/URS0000AB94B2/358681" target="_blank" rel="noopener noreferrer">RNAcentral</a>   |
| <span title="ID within respective databases">ID</span>  | 5HSAA033225     | URS000231FE77_682795     | URS0000E23FFC_1339248     | URS0000AB94B2_358681     |
| <span title="Length of the sequence in question">Length</span>  | 172     |  171    | 173   |  171    |
| <span title="Similarity score calculated from all similarity metrics">Similarity</span>  | - | 0.96 | 0.96 | 0.96 |
| <span title="Ensemble classification via all 19 ML classifiers">Ensemble Norm</span>  | 0.96 | - | - | - |
| <span title="Nupack Mean Free Energy of the secondary structure">MFE</span>  | -48.17 | -49.07 | -66.97 | -59.65 |
| <span title="Reported Ligand match on RNAcentral or via RFAM">Ligands</span>  | - | cobalamin | glucosamine | glucosamine |
| <span title="Homo Sapiens gene abbreviation">Gene</span>  | EDA | - | - | - |
| <span title="Link to the sequence source">Downstream protein</span>  | <a href="https://www.genecards.org/cgi-bin/carddisp.pl?gene=EDA" target="_blank" rel="noopener noreferrer"> Genecard </a>   |    -    | -  | - |


**Similarity metrics**

| | 5'UTR       | RS match 1   | RS match 2  | RS match 3 |
| ---- | ----------- | ----------- | ----------- | ----------- |
| <span title="Structural feature squared error">Struct SE</span> | - | 4 | 6 | 8 |
| <span title="Length difference squared error">Length SE</span> | - | 1 | 1 | 1 |
| <span title="Edit distance of both dot structures">Lev Distance</span> | - | 54 | 59 | 58 |
| <span title="Unbranched stack count">UBS</span>| 12 | 12 | 10 | 11 |
| <span title="Branched stack counts">BS</span> | 0 | 0 | 0 | 0 |
| <span title="Inner loop left count">ILL</span> | 1 | 2 | 1 | 2 |
| <span title="Inner loop right count">ILR</span> | 4 | 3 | 3 | 2 |
| <span title="Hairpin counts">H</span> | 6 | 6 | 5 | 5 |
| <span title="Bulges left count">BL</span> | 2 | 3 | 2 | 3 |
| <span title="Bulges right count">BR</span> | 2 | 3 | 2 | 2 |
| <span title="Unpaired nucleotide %">UN</span> | 0.11 | 0.16 | 0.14 | 0.12 |

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
<td markdown="span"> UCAUUUUUUCAAGCGCCAGAACUAGGCCCUGGGACGUGCGGGGGCUUAGUUGACGAGGUGGAGGUUUAUCGAGGUGUUCGGCGGAUGCCUCCCGGCUGUGCACACGCAGUCGAGAGCCAUCUUCCCAAAACAUUAAGGCGACUUAAUGGACAAAGGAAGAUGGAAGGUGUGCG
</td>
</tr>


<tr>
<td markdown="span">RS 2 dot </td>
<td markdown="span"> .............((((.((((((((((((.(......).)))))))))))..)..))))((......))(((((((((...)))))))))(((((((((....)))))))).)..(((((((((.....(((((((....)))))))......)))))))))..........
</td>
</tr>


<tr>
<td markdown="span">RS 3 seq </td>
<td markdown="span"> UACCAUUGGAAAGCGCCAGCACUGAGGCUGCCCGACAUGGAGCCCAGUGGACGAGGUGGAGGUUUAUCGAAGCAUUCGGCGGAUACCUCCCGGCAGCAGUAUCACUGCCGCAGAGCGCAGGGACAAAACAUCAGGGUGAUCUGAUGGACAAAACCUUGUGUGUGAUACGUU
</td>
</tr>


<tr>
<td markdown="span">RS 3 dot </td>
<td markdown="span"> .....((((......))))(((((.((((.((......)))))))))))........((((((((.(((((...)))))..)).))))))((((((........))))))((..((((((((......(((((((....))))))).......)))))))).)).......
</td>
</tr>

</tbody>
</table>


</div>


[Back to Ensemble of 20 Table](../../display_436)

[Back to Ensemble of 1 Table](../../display_1533)
