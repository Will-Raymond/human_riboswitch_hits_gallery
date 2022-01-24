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
<th>Ensemble score</th>
<th>aln percent</th>
<th>Visualization</th>
</tr>
</thead>
<tbody>
<tr>
<td>CARKD</td>
<td>5HSAA016976</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA016976/1">UTR</a></td>
<td>URS0000AB6657_332952</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6657/332952">RS</a></td>
<td>3.788</td>
<td>0.23374982</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CARKD">=></a></td>
</tr>
<tr>
<td>RBM46</td>
<td>5HSAA089522</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089522/1">UTR</a></td>
<td>URS0000AB4B53_3068</td>
<td><a href="https://rnacentral.org/rna/URS0000AB4B53/3068">RS</a></td>
<td>4.023</td>
<td>0.22847083</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RBM46">=></a></td>
</tr>
<tr>
<td>C4ORF45</td>
<td>5HSAA014981</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA014981/1">UTR</a></td>
<td>URS0000C3A689_28573</td>
<td><a href="https://rnacentral.org/rna/URS0000C3A689/28573">RS</a></td>
<td>3.906</td>
<td>0.22123831</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C4ORF45">=></a></td>
</tr>
<tr>
<td>TMBIM6</td>
<td>5HSAA110075</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA110075/1">UTR</a></td>
<td>URS0000BFA3F1_701091</td>
<td><a href="https://rnacentral.org/rna/URS0000BFA3F1/701091">RS</a></td>
<td>2.647</td>
<td>0.22070703</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMBIM6">=></a></td>
</tr>
<tr>
<td>NAT5</td>
<td>5HSAA070288</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA070288/1">UTR</a></td>
<td>URS0000C5DB95_1043002</td>
<td><a href="https://rnacentral.org/rna/URS0000C5DB95/1043002">RS</a></td>
<td>3.765</td>
<td>0.21262641</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NAT5">=></a></td>
</tr>
<tr>
<td>RPL29</td>
<td>5HSAA092526</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092526/1">UTR</a></td>
<td>URS0000C19CFE_1069680</td>
<td><a href="https://rnacentral.org/rna/URS0000C19CFE/1069680">RS</a></td>
<td>2.359</td>
<td>0.209214</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL29">=></a></td>
</tr>
<tr>
<td>RAB33A</td>
<td>5HSAA087442</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA087442/1">UTR</a></td>
<td>URS0000D8EB09_1408157</td>
<td><a href="https://rnacentral.org/rna/URS0000D8EB09/1408157">RS</a></td>
<td>2.815</td>
<td>0.20310487</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RAB33A">=></a></td>
</tr>
<tr>
<td>EIF4G1</td>
<td>5HSAA034595</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA034595/1">UTR</a></td>
<td>URS0000C4C8AA_1214573</td>
<td><a href="https://rnacentral.org/rna/URS0000C4C8AA/1214573">RS</a></td>
<td>3.013</td>
<td>0.1951366</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF4G1">=></a></td>
</tr>
<tr>
<td>DMP1</td>
<td>5HSAA030716</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA030716/1">UTR</a></td>
<td>URS000020A25D_3562</td>
<td><a href="https://rnacentral.org/rna/URS000020A25D/3562">RS</a></td>
<td>2.294</td>
<td>0.19433923</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DMP1">=></a></td>
</tr>
<tr>
<td>MAP2K4</td>
<td>5HSAA062296</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA062296/1">UTR</a></td>
<td>URS0000ABD54F_398673</td>
<td><a href="https://rnacentral.org/rna/URS0000ABD54F/398673">RS</a></td>
<td>2.164</td>
<td>0.19326988</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAP2K4">=></a></td>
</tr>
<tr>
<td>CPEB3</td>
<td>5HSAA024654</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024654/1">UTR</a></td>
<td>URS0000C7468E_383855</td>
<td><a href="https://rnacentral.org/rna/URS0000C7468E/383855">RS</a></td>
<td>2.484</td>
<td>0.19308775</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CPEB3">=></a></td>
</tr>
<tr>
<td>COPB2</td>
<td>5HSAA024186</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024186/1">UTR</a></td>
<td>URS0000D865AA_33097</td>
<td><a href="https://rnacentral.org/rna/URS0000D865AA/33097">RS</a></td>
<td>4.958</td>
<td>0.19290804</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COPB2">=></a></td>
</tr>
<tr>
<td>SUSD3</td>
<td>5HSAA106103</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA106103/1">UTR</a></td>
<td>URS0000C3AF45_765868</td>
<td><a href="https://rnacentral.org/rna/URS0000C3AF45/765868">RS</a></td>
<td>4.87</td>
<td>0.18908422</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SUSD3">=></a></td>
</tr>
<tr>
<td>EIF2B2</td>
<td>5HSAA033935</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033935/1">UTR</a></td>
<td>URS0000C2E7C3_3988</td>
<td><a href="https://rnacentral.org/rna/URS0000C2E7C3/3988">RS</a></td>
<td>2.477</td>
<td>0.18819242</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF2B2">=></a></td>
</tr>
<tr>
<td>IGHMBP2</td>
<td>5HSAA052101</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA052101/1">UTR</a></td>
<td>URS00009FC17C_79923</td>
<td><a href="https://rnacentral.org/rna/URS00009FC17C/79923">RS</a></td>
<td>3.563</td>
<td>0.18436595</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IGHMBP2">=></a></td>
</tr>
<tr>
<td>SAMD13</td>
<td>5HSAA094053</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA094053/1">UTR</a></td>
<td>URS0000C49CC4_4572</td>
<td><a href="https://rnacentral.org/rna/URS0000C49CC4/4572">RS</a></td>
<td>2.072</td>
<td>0.18354958</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SAMD13">=></a></td>
</tr>
<tr>
<td>CTNNB1</td>
<td>5HSAA026218</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA026218/1">UTR</a></td>
<td>URS0000AB6626_660122</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6626/660122">RS</a></td>
<td>4.492</td>
<td>0.18000419</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CTNNB1">=></a></td>
</tr>
<tr>
<td>LOC389203</td>
<td>5HSAA059740</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059740/1">UTR</a></td>
<td>URS0000AB421D_331117</td>
<td><a href="https://rnacentral.org/rna/URS0000AB421D/331117">RS</a></td>
<td>3.379</td>
<td>0.17391099</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LOC389203">=></a></td>
</tr>
<tr>
<td>ZNF791</td>
<td>5HSAA123955</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123955/1">UTR</a></td>
<td>URS0000C192F0_765440</td>
<td><a href="https://rnacentral.org/rna/URS0000C192F0/765440">RS</a></td>
<td>2.971</td>
<td>0.16911145</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF791">=></a></td>
</tr>
<tr>
<td>PPFIA1</td>
<td>5HSAA083103</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083103/1">UTR</a></td>
<td>URS0000C77DD5_1524831</td>
<td><a href="https://rnacentral.org/rna/URS0000C77DD5/1524831">RS</a></td>
<td>4.123</td>
<td>0.16880314</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPFIA1">=></a></td>
</tr>
<tr>
<td>NOSTRIN</td>
<td>5HSAA072901</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072901/1">UTR</a></td>
<td>URS0000D8EB8E_93759</td>
<td><a href="https://rnacentral.org/rna/URS0000D8EB8E/93759">RS</a></td>
<td>3.943</td>
<td>0.16854019</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NOSTRIN">=></a></td>
</tr>
<tr>
<td>CD53</td>
<td>5HSAA019892</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA019892/1">UTR</a></td>
<td>URS0000BF58B7_1283841</td>
<td><a href="https://rnacentral.org/rna/URS0000BF58B7/1283841">RS</a></td>
<td>2.953</td>
<td>0.16812376</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CD53">=></a></td>
</tr>
<tr>
<td>FKBP6</td>
<td>5HSAA041148</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA041148/1">UTR</a></td>
<td>URS0000C07AC7_308745</td>
<td><a href="https://rnacentral.org/rna/URS0000C07AC7/308745">RS</a></td>
<td>2.558</td>
<td>0.16424605</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FKBP6">=></a></td>
</tr>
<tr>
<td>VAV3</td>
<td>5HSAA118078</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA118078/1">UTR</a></td>
<td>URS0000C070E4_157072</td>
<td><a href="https://rnacentral.org/rna/URS0000C070E4/157072">RS</a></td>
<td>1.654</td>
<td>0.16422443</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/VAV3">=></a></td>
</tr>
<tr>
<td>CCDC76</td>
<td>5HSAA018656</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018656/1">UTR</a></td>
<td>URS0000DB63AA_93759</td>
<td><a href="https://rnacentral.org/rna/URS0000DB63AA/93759">RS</a></td>
<td>3.56</td>
<td>0.16255007</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC76">=></a></td>
</tr>
<tr>
<td>C8ORF59</td>
<td>5HSAA015592</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA015592/1">UTR</a></td>
<td>URS0000C228F8_1220926</td>
<td><a href="https://rnacentral.org/rna/URS0000C228F8/1220926">RS</a></td>
<td>3.381</td>
<td>0.16149897</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C8ORF59">=></a></td>
</tr>
<tr>
<td>SAT1</td>
<td>5HSAA094521</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA094521/1">UTR</a></td>
<td>URS0000C2BA30_1081102</td>
<td><a href="https://rnacentral.org/rna/URS0000C2BA30/1081102">RS</a></td>
<td>2.154</td>
<td>0.15977004</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SAT1">=></a></td>
</tr>
<tr>
<td>DPH3</td>
<td>5HSAA031935</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA031935/1">UTR</a></td>
<td>URS0000C41E64_12930</td>
<td><a href="https://rnacentral.org/rna/URS0000C41E64/12930">RS</a></td>
<td>4.517</td>
<td>0.1595892</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DPH3">=></a></td>
</tr>
<tr>
<td>WFDC3</td>
<td>5HSAA119784</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA119784/1">UTR</a></td>
<td>URS0000C43551_4572</td>
<td><a href="https://rnacentral.org/rna/URS0000C43551/4572">RS</a></td>
<td>1.992</td>
<td>0.15895357</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/WFDC3">=></a></td>
</tr>
<tr>
<td>C14ORF100</td>
<td>5HSAA012369</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA012369/1">UTR</a></td>
<td>URS0000C3BEEE_183478</td>
<td><a href="https://rnacentral.org/rna/URS0000C3BEEE/183478">RS</a></td>
<td>2.297</td>
<td>0.15802201</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C14ORF100">=></a></td>
</tr>
<tr>
<td>TTC23</td>
<td>5HSAA114686</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114686/1">UTR</a></td>
<td>URS0000BEFA03_1344418</td>
<td><a href="https://rnacentral.org/rna/URS0000BEFA03/1344418">RS</a></td>
<td>1.915</td>
<td>0.15328845</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TTC23">=></a></td>
</tr>
<tr>
<td>TRMT5</td>
<td>5HSAA113890</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA113890/1">UTR</a></td>
<td>URS0000ABBC28_502780</td>
<td><a href="https://rnacentral.org/rna/URS0000ABBC28/502780">RS</a></td>
<td>4.948</td>
<td>0.15314932</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TRMT5">=></a></td>
</tr>
<tr>
<td>PPPDE2</td>
<td>5HSAA084001</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA084001/1">UTR</a></td>
<td>URS0000C73A13_5802</td>
<td><a href="https://rnacentral.org/rna/URS0000C73A13/5802">RS</a></td>
<td>2.949</td>
<td>0.14886944</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPPDE2">=></a></td>
</tr>
<tr>
<td>PIGA</td>
<td>5HSAA080156</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080156/1">UTR</a></td>
<td>URS0000C07AC7_308745</td>
<td><a href="https://rnacentral.org/rna/URS0000C07AC7/308745">RS</a></td>
<td>3.374</td>
<td>0.14678556</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PIGA">=></a></td>
</tr>
<tr>
<td>GNAS</td>
<td>5HSAA045060</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA045060/1">UTR</a></td>
<td>URS0000C6E47E_765868</td>
<td><a href="https://rnacentral.org/rna/URS0000C6E47E/765868">RS</a></td>
<td>3.89</td>
<td>0.14499685</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GNAS">=></a></td>
</tr>
<tr>
<td>RPS24</td>
<td>5HSAA092962</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092962/1">UTR</a></td>
<td>URS0000C7CB5E_293939</td>
<td><a href="https://rnacentral.org/rna/URS0000C7CB5E/293939">RS</a></td>
<td>3.029</td>
<td>0.1443609</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS24">=></a></td>
</tr>
<tr>
<td>TMX2</td>
<td>5HSAA111796</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111796/1">UTR</a></td>
<td>URS0000C06CB4_9209</td>
<td><a href="https://rnacentral.org/rna/URS0000C06CB4/9209">RS</a></td>
<td>2.776</td>
<td>0.14325599</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMX2">=></a></td>
</tr>
<tr>
<td>HNRNPH2</td>
<td>5HSAA050075</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050075/1">UTR</a></td>
<td>URS0000BEBE94_1314783</td>
<td><a href="https://rnacentral.org/rna/URS0000BEBE94/1314783">RS</a></td>
<td>2.089</td>
<td>0.14215216</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HNRNPH2">=></a></td>
</tr>
<tr>
<td>STAMBP</td>
<td>5HSAA104444</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA104444/1">UTR</a></td>
<td>URS0000C71E12_1460663</td>
<td><a href="https://rnacentral.org/rna/URS0000C71E12/1460663">RS</a></td>
<td>4.517</td>
<td>0.14132501</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/STAMBP">=></a></td>
</tr>
<tr>
<td>CEPT1</td>
<td>5HSAA021163</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA021163/1">UTR</a></td>
<td>URS0000BFA481_1287680</td>
<td><a href="https://rnacentral.org/rna/URS0000BFA481/1287680">RS</a></td>
<td>3.85</td>
<td>0.1394723</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CEPT1">=></a></td>
</tr>
<tr>
<td>AURKC</td>
<td>5HSAA009080</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA009080/1">UTR</a></td>
<td>URS0000D856CD_2951</td>
<td><a href="https://rnacentral.org/rna/URS0000D856CD/2951">RS</a></td>
<td>2.727</td>
<td>0.13831413</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AURKC">=></a></td>
</tr>
<tr>
<td>C2ORF77</td>
<td>5HSAA014640</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA014640/1">UTR</a></td>
<td>URS0000C84A7A_13735</td>
<td><a href="https://rnacentral.org/rna/URS0000C84A7A/13735">RS</a></td>
<td>2.973</td>
<td>0.13754534</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C2ORF77">=></a></td>
</tr>
<tr>
<td>GTF2F1</td>
<td>5HSAA047224</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047224/1">UTR</a></td>
<td>URS0000C5AF96_1622149</td>
<td><a href="https://rnacentral.org/rna/URS0000C5AF96/1622149">RS</a></td>
<td>3.294</td>
<td>0.13722956</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GTF2F1">=></a></td>
</tr>
<tr>
<td>LINGO2</td>
<td>5HSAA059119</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059119/1">UTR</a></td>
<td>URS0000C7D6F3_10181</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D6F3/10181">RS</a></td>
<td>3.139</td>
<td>0.13337013</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LINGO2">=></a></td>
</tr>
<tr>
<td>TCEAL8</td>
<td>5HSAA107637</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA107637/1">UTR</a></td>
<td>URS0000C7D6F3_10181</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D6F3/10181">RS</a></td>
<td>2.807</td>
<td>0.1311013</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TCEAL8">=></a></td>
</tr>
<tr>
<td>TYW3</td>
<td>5HSAA115490</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115490/1">UTR</a></td>
<td>URS0000C2C567_1437433</td>
<td><a href="https://rnacentral.org/rna/URS0000C2C567/1437433">RS</a></td>
<td>2.662</td>
<td>0.12933421</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TYW3">=></a></td>
</tr>
<tr>
<td>HIPK3</td>
<td>5HSAA049231</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049231/1">UTR</a></td>
<td>URS0000C43551_4572</td>
<td><a href="https://rnacentral.org/rna/URS0000C43551/4572">RS</a></td>
<td>3.916</td>
<td>0.12815033</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HIPK3">=></a></td>
</tr>
<tr>
<td>LRP2</td>
<td>5HSAA060316</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA060316/1">UTR</a></td>
<td>URS0000C5C273_983967</td>
<td><a href="https://rnacentral.org/rna/URS0000C5C273/983967">RS</a></td>
<td>2.154</td>
<td>0.12577519</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LRP2">=></a></td>
</tr>
<tr>
<td>RANGRF</td>
<td>5HSAA088659</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA088659/1">UTR</a></td>
<td>URS0000AB6659_644358</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6659/644358">RS</a></td>
<td>2.949</td>
<td>0.12520961</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RANGRF">=></a></td>
</tr>
<tr>
<td>ZNF808</td>
<td>5HSAA123978</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123978/1">UTR</a></td>
<td>URS0000D8EB8E_93759</td>
<td><a href="https://rnacentral.org/rna/URS0000D8EB8E/93759">RS</a></td>
<td>2.83</td>
<td>0.1223437</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF808">=></a></td>
</tr>
<tr>
<td>ZDHHC20</td>
<td>5HSAA121384</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA121384/1">UTR</a></td>
<td>URS0000D790E9_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000D790E9/3562">RS</a></td>
<td>2.961</td>
<td>0.12229083</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZDHHC20">=></a></td>
</tr>
<tr>
<td>VPS35</td>
<td>5HSAA118436</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA118436/1">UTR</a></td>
<td>URS0000C41E64_12930</td>
<td><a href="https://rnacentral.org/rna/URS0000C41E64/12930">RS</a></td>
<td>2.737</td>
<td>0.12197092</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/VPS35">=></a></td>
</tr>
<tr>
<td>IQCG</td>
<td>5HSAA053716</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA053716/1">UTR</a></td>
<td>URS0000AB3CEA_861557</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3CEA/861557">RS</a></td>
<td>3.862</td>
<td>0.12113382</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IQCG">=></a></td>
</tr>
<tr>
<td>RTF1</td>
<td>5HSAA093544</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093544/1">UTR</a></td>
<td>URS0000AB2F20_871575</td>
<td><a href="https://rnacentral.org/rna/URS0000AB2F20/871575">RS</a></td>
<td>2.91</td>
<td>0.12034739</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RTF1">=></a></td>
</tr>
<tr>
<td>EIF3H</td>
<td>5HSAA034275</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA034275/1">UTR</a></td>
<td>URS0000C4A992_857566</td>
<td><a href="https://rnacentral.org/rna/URS0000C4A992/857566">RS</a></td>
<td>3.83</td>
<td>0.1122458</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF3H">=></a></td>
</tr>
<tr>
<td>BNIP2</td>
<td>5HSAA010809</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010809/1">UTR</a></td>
<td>URS0000DA819D_44415</td>
<td><a href="https://rnacentral.org/rna/URS0000DA819D/44415">RS</a></td>
<td>2.444</td>
<td>0.11190836</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BNIP2">=></a></td>
</tr>
<tr>
<td>SDF4</td>
<td>5HSAA095446</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095446/1">UTR</a></td>
<td>URS0000D7A00E_4432</td>
<td><a href="https://rnacentral.org/rna/URS0000D7A00E/4432">RS</a></td>
<td>2.785</td>
<td>0.11173913</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SDF4">=></a></td>
</tr>
<tr>
<td>ENY2</td>
<td>5HSAA035641</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035641/1">UTR</a></td>
<td>URS0000C8A0C3_104259</td>
<td><a href="https://rnacentral.org/rna/URS0000C8A0C3/104259">RS</a></td>
<td>2.952</td>
<td>0.11115496</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ENY2">=></a></td>
</tr>
<tr>
<td>RPE</td>
<td>5HSAA092279</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092279/1">UTR</a></td>
<td>URS0000ABD0D2_30025</td>
<td><a href="https://rnacentral.org/rna/URS0000ABD0D2/30025">RS</a></td>
<td>3.583</td>
<td>0.11057692</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPE">=></a></td>
</tr>
<tr>
<td>UBL5</td>
<td>5HSAA116393</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA116393/1">UTR</a></td>
<td>URS0000C1F787_1182541</td>
<td><a href="https://rnacentral.org/rna/URS0000C1F787/1182541">RS</a></td>
<td>2.352</td>
<td>0.10966981</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBL5">=></a></td>
</tr>
<tr>
<td>LETM2</td>
<td>5HSAA058662</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA058662/1">UTR</a></td>
<td>URS0000BFF8EE_1296100</td>
<td><a href="https://rnacentral.org/rna/URS0000BFF8EE/1296100">RS</a></td>
<td>2.533</td>
<td>0.10836795</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LETM">=></a></td>
</tr>
<tr>
<td>DLK2</td>
<td>5HSAA030650</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA030650/1">UTR</a></td>
<td>URS0000D782C1_1519565</td>
<td><a href="https://rnacentral.org/rna/URS0000D782C1/1519565">RS</a></td>
<td>2.234</td>
<td>0.10770124</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DLK2">=></a></td>
</tr>
<tr>
<td>ST6GAL2</td>
<td>5HSAA104249</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA104249/1">UTR</a></td>
<td>URS0000AB93AD_341663</td>
<td><a href="https://rnacentral.org/rna/URS0000AB93AD/341663">RS</a></td>
<td>3.499</td>
<td>0.10685267</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ST6GAL2">=></a></td>
</tr>
<tr>
<td>GTF2F1</td>
<td>5HSAA047231</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047231/1">UTR</a></td>
<td>URS0000A5F9D7_6945</td>
<td><a href="https://rnacentral.org/rna/URS0000A5F9D7/6945">RS</a></td>
<td>2.467</td>
<td>0.10659466</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GTF2F1">=></a></td>
</tr>
<tr>
<td>ARFGEF2</td>
<td>5HSAA006050</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA006050/1">UTR</a></td>
<td>URS0000AB3AE6_214684</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3AE6/214684">RS</a></td>
<td>2.826</td>
<td>0.10653763</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ARFGEF2">=></a></td>
</tr>
<tr>
<td>NOP2</td>
<td>5HSAA072814</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072814/1">UTR</a></td>
<td>URS0000C052F9_1420901</td>
<td><a href="https://rnacentral.org/rna/URS0000C052F9/1420901">RS</a></td>
<td>2.97</td>
<td>0.10559921</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NOP2">=></a></td>
</tr>
<tr>
<td>ADARB1</td>
<td>5HSAA002206</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA002206/1">UTR</a></td>
<td>URS0000C1B90E_36087</td>
<td><a href="https://rnacentral.org/rna/URS0000C1B90E/36087">RS</a></td>
<td>2.436</td>
<td>0.10537975</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ADARB1">=></a></td>
</tr>
<tr>
<td>TTC23</td>
<td>5HSAA114692</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114692/1">UTR</a></td>
<td>URS0000C64B2D_98403</td>
<td><a href="https://rnacentral.org/rna/URS0000C64B2D/98403">RS</a></td>
<td>3.831</td>
<td>0.10528822</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TTC23">=></a></td>
</tr>
<tr>
<td>GAS7</td>
<td>5HSAA043315</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA043315/1">UTR</a></td>
<td>URS0000ABD0D2_30025</td>
<td><a href="https://rnacentral.org/rna/URS0000ABD0D2/30025">RS</a></td>
<td>2.723</td>
<td>0.10331033</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GAS7">=></a></td>
</tr>
<tr>
<td>GTF2A1</td>
<td>5HSAA047177</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047177/1">UTR</a></td>
<td>URS0000BEBE94_1314783</td>
<td><a href="https://rnacentral.org/rna/URS0000BEBE94/1314783">RS</a></td>
<td>2.12</td>
<td>0.10287868</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GTF2A1">=></a></td>
</tr>
<tr>
<td>PEX11B</td>
<td>5HSAA078949</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA078949/1">UTR</a></td>
<td>URS0000DB1FE6_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000DB1FE6/3562">RS</a></td>
<td>4.555</td>
<td>0.10274077</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PEX11B">=></a></td>
</tr>
<tr>
<td>DPH2</td>
<td>5HSAA031933</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA031933/1">UTR</a></td>
<td>URS0000D831B7_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000D831B7/3562">RS</a></td>
<td>2.586</td>
<td>0.10225605</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DPH2">=></a></td>
</tr>
<tr>
<td>LIG3</td>
<td>5HSAA058928</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA058928/1">UTR</a></td>
<td>URS0000D7C9F0_416450</td>
<td><a href="https://rnacentral.org/rna/URS0000D7C9F0/416450">RS</a></td>
<td>2.374</td>
<td>0.10191476</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LIG3">=></a></td>
</tr>
<tr>
<td>C9ORF61</td>
<td>5HSAA015776</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA015776/1">UTR</a></td>
<td>URS0000D856CD_2951</td>
<td><a href="https://rnacentral.org/rna/URS0000D856CD/2951">RS</a></td>
<td>2.383</td>
<td>0.10122267</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C9ORF61">=></a></td>
</tr>
<tr>
<td>NRBP1</td>
<td>5HSAA073358</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA073358/1">UTR</a></td>
<td>URS0000C28514_109478</td>
<td><a href="https://rnacentral.org/rna/URS0000C28514/109478">RS</a></td>
<td>2.7</td>
<td>0.10039784</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NRBP1">=></a></td>
</tr>
<tr>
<td>ZNF321</td>
<td>5HSAA122639</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA122639/1">UTR</a></td>
<td>URS0000BFE4BA_4572</td>
<td><a href="https://rnacentral.org/rna/URS0000BFE4BA/4572">RS</a></td>
<td>3.973</td>
<td>0.09936496</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF321">=></a></td>
</tr>
<tr>
<td>BMX</td>
<td>5HSAA010795</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010795/1">UTR</a></td>
<td>URS0000D7A33C_93759</td>
<td><a href="https://rnacentral.org/rna/URS0000D7A33C/93759">RS</a></td>
<td>4.852</td>
<td>0.09845423</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BMX">=></a></td>
</tr>
<tr>
<td>ARHGAP24</td>
<td>5HSAA006211</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA006211/1">UTR</a></td>
<td>URS0000BEFF82_671987</td>
<td><a href="https://rnacentral.org/rna/URS0000BEFF82/671987">RS</a></td>
<td>2.639</td>
<td>0.09809227</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ARHGAP24">=></a></td>
</tr>
<tr>
<td>NIF3L1</td>
<td>5HSAA072156</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072156/1">UTR</a></td>
<td>URS0000C4FDA4_1509407</td>
<td><a href="https://rnacentral.org/rna/URS0000C4FDA4/1509407">RS</a></td>
<td>3.761</td>
<td>0.09707322</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NIF3L1">=></a></td>
</tr>
<tr>
<td>TPK1</td>
<td>5HSAA112772</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA112772/1">UTR</a></td>
<td>URS0000C84F9C_1245745</td>
<td><a href="https://rnacentral.org/rna/URS0000C84F9C/1245745">RS</a></td>
<td>2.057</td>
<td>0.09627971</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TPK1">=></a></td>
</tr>
<tr>
<td>SPINK5</td>
<td>5HSAA103327</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103327/1">UTR</a></td>
<td>URS0000C09C7B_6265</td>
<td><a href="https://rnacentral.org/rna/URS0000C09C7B/6265">RS</a></td>
<td>2.321</td>
<td>0.09617663</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPINK5">=></a></td>
</tr>
<tr>
<td>C19ORF50</td>
<td>5HSAA013374</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA013374/1">UTR</a></td>
<td>URS0000D7BC27_106004</td>
<td><a href="https://rnacentral.org/rna/URS0000D7BC27/106004">RS</a></td>
<td>2.023</td>
<td>0.09598763</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C19ORF50">=></a></td>
</tr>
<tr>
<td>BTD</td>
<td>5HSAA011273</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA011273/1">UTR</a></td>
<td>URS0000D9EC9F_201502</td>
<td><a href="https://rnacentral.org/rna/URS0000D9EC9F/201502">RS</a></td>
<td>1.681</td>
<td>0.09491258</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BTD">=></a></td>
</tr>
<tr>
<td>UBAP2L</td>
<td>5HSAA115944</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115944/1">UTR</a></td>
<td>URS0000C52734_471704</td>
<td><a href="https://rnacentral.org/rna/URS0000C52734/471704">RS</a></td>
<td>3.371</td>
<td>0.09451313</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBAP2L">=></a></td>
</tr>
<tr>
<td>TTBK2</td>
<td>5HSAA114526</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114526/1">UTR</a></td>
<td>URS0000DA3D0F_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000DA3D0F/3562">RS</a></td>
<td>3.654</td>
<td>0.09422809</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TTBK2">=></a></td>
</tr>
<tr>
<td>ZNF585B</td>
<td>5HSAA123463</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123463/1">UTR</a></td>
<td>URS0000DB4A81_4232</td>
<td><a href="https://rnacentral.org/rna/URS0000DB4A81/4232">RS</a></td>
<td>2.658</td>
<td>0.09377397</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF585B">=></a></td>
</tr>
<tr>
<td>NRBP1</td>
<td>5HSAA073360</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA073360/1">UTR</a></td>
<td>URS0000AB4DD2_39946</td>
<td><a href="https://rnacentral.org/rna/URS0000AB4DD2/39946">RS</a></td>
<td>2.45</td>
<td>0.09369464</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NRBP1">=></a></td>
</tr>
<tr>
<td>PLA2G15</td>
<td>5HSAA080777</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080777/1">UTR</a></td>
<td>URS0000D9035E_1813822</td>
<td><a href="https://rnacentral.org/rna/URS0000D9035E/1813822">RS</a></td>
<td>2.629</td>
<td>0.09339298</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PLA2G15">=></a></td>
</tr>
<tr>
<td>MYL12A</td>
<td>5HSAA069191</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA069191/1">UTR</a></td>
<td>URS0000BE8919_1314781</td>
<td><a href="https://rnacentral.org/rna/URS0000BE8919/1314781">RS</a></td>
<td>1.992</td>
<td>0.09013766</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MYL12A">=></a></td>
</tr>
<tr>
<td>IRAK1BP1</td>
<td>5HSAA053795</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA053795/1">UTR</a></td>
<td>URS0000DA819D_44415</td>
<td><a href="https://rnacentral.org/rna/URS0000DA819D/44415">RS</a></td>
<td>4.495</td>
<td>0.08994209</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IRAK1BP1">=></a></td>
</tr>
<tr>
<td>RSRC1</td>
<td>5HSAA093483</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093483/1">UTR</a></td>
<td>URS0000AB5B4E_45351</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5B4E/45351">RS</a></td>
<td>3.0</td>
<td>0.08969622</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RSRC1">=></a></td>
</tr>
<tr>
<td>LAMP3</td>
<td>5HSAA057811</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057811/1">UTR</a></td>
<td>URS0000C5DB95_1043002</td>
<td><a href="https://rnacentral.org/rna/URS0000C5DB95/1043002">RS</a></td>
<td>2.036</td>
<td>0.08931611</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LAMP3">=></a></td>
</tr>
<tr>
<td>DNAJC24</td>
<td>5HSAA031075</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA031075/1">UTR</a></td>
<td>URS0000D7F147_22663</td>
<td><a href="https://rnacentral.org/rna/URS0000D7F147/22663">RS</a></td>
<td>3.23</td>
<td>0.08909915</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DNAJC24">=></a></td>
</tr>
<tr>
<td>CCDC108</td>
<td>5HSAA018190</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018190/1">UTR</a></td>
<td>URS0000C1C7DA_8496</td>
<td><a href="https://rnacentral.org/rna/URS0000C1C7DA/8496">RS</a></td>
<td>2.174</td>
<td>0.08878745</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC108">=></a></td>
</tr>
<tr>
<td>EGR3</td>
<td>5HSAA033711</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033711/1">UTR</a></td>
<td>URS0000C7D6F3_10181</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D6F3/10181">RS</a></td>
<td>3.909</td>
<td>0.0879323</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EGR3">=></a></td>
</tr>
<tr>
<td>LYSMD4</td>
<td>5HSAA061223</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA061223/1">UTR</a></td>
<td>URS0000C1302D_77166</td>
<td><a href="https://rnacentral.org/rna/URS0000C1302D/77166">RS</a></td>
<td>2.432</td>
<td>0.08584155</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LYSMD4">=></a></td>
</tr>
<tr>
<td>GTPBP6</td>
<td>5HSAA047442</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047442/1">UTR</a></td>
<td>URS0000BE2C05_67767</td>
<td><a href="https://rnacentral.org/rna/URS0000BE2C05/67767">RS</a></td>
<td>3.925</td>
<td>0.08455012</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GTPBP6">=></a></td>
</tr>
<tr>
<td>GHITM</td>
<td>5HSAA044078</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA044078/1">UTR</a></td>
<td>URS0000AB5878_284591</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5878/284591">RS</a></td>
<td>2.76</td>
<td>0.08385965</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GHITM">=></a></td>
</tr>
<tr>
<td>INADL</td>
<td>5HSAA053020</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA053020/1">UTR</a></td>
<td>URS0000B1F654_1230383</td>
<td><a href="https://rnacentral.org/rna/URS0000B1F654/1230383">RS</a></td>
<td>2.302</td>
<td>0.08209818</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/INADL">=></a></td>
</tr>
<tr>
<td>LIPT1</td>
<td>5HSAA059169</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059169/1">UTR</a></td>
<td>URS0000DB47F2_767769</td>
<td><a href="https://rnacentral.org/rna/URS0000DB47F2/767769">RS</a></td>
<td>2.178</td>
<td>0.08205188</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LIPT1">=></a></td>
</tr>
<tr>
<td>TXLNB</td>
<td>5HSAA115309</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115309/1">UTR</a></td>
<td>URS0000D82970_201502</td>
<td><a href="https://rnacentral.org/rna/URS0000D82970/201502">RS</a></td>
<td>1.629</td>
<td>0.08173108</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TXLNB">=></a></td>
</tr>
<tr>
<td>SNX13</td>
<td>5HSAA102139</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA102139/1">UTR</a></td>
<td>URS0000D7BC27_106004</td>
<td><a href="https://rnacentral.org/rna/URS0000D7BC27/106004">RS</a></td>
<td>3.155</td>
<td>0.08102084</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SNX13">=></a></td>
</tr>
<tr>
<td>SFRS5</td>
<td>5HSAA097407</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA097407/1">UTR</a></td>
<td>URS0000C33634_1213857</td>
<td><a href="https://rnacentral.org/rna/URS0000C33634/1213857">RS</a></td>
<td>3.218</td>
<td>0.08034682</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SFRS5">=></a></td>
</tr>
<tr>
<td>RIMKLB</td>
<td>5HSAA091043</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA091043/1">UTR</a></td>
<td>URS0000C43551_4572</td>
<td><a href="https://rnacentral.org/rna/URS0000C43551/4572">RS</a></td>
<td>4.901</td>
<td>0.08032424</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RIMKLB">=></a></td>
</tr>
<tr>
<td>QKI</td>
<td>5HSAA087117</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA087117/1">UTR</a></td>
<td>URS0000C09C7B_6265</td>
<td><a href="https://rnacentral.org/rna/URS0000C09C7B/6265">RS</a></td>
<td>3.995</td>
<td>0.0784417</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/QKI">=></a></td>
</tr>
<tr>
<td>SLC35A5</td>
<td>5HSAA099878</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA099878/1">UTR</a></td>
<td>URS0000C4A631_3848</td>
<td><a href="https://rnacentral.org/rna/URS0000C4A631/3848">RS</a></td>
<td>3.595</td>
<td>0.07828215</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SLC35A5">=></a></td>
</tr>
<tr>
<td>ATP10A</td>
<td>5HSAA008224</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA008224/1">UTR</a></td>
<td>URS0000AB42B7_10181</td>
<td><a href="https://rnacentral.org/rna/URS0000AB42B7/10181">RS</a></td>
<td>2.483</td>
<td>0.07783936</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ATP10A">=></a></td>
</tr>
<tr>
<td>CITED2</td>
<td>5HSAA022175</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA022175/1">UTR</a></td>
<td>URS0000DB669E_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000DB669E/3562">RS</a></td>
<td>1.445</td>
<td>0.07746962</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CITED2">=></a></td>
</tr>
<tr>
<td>C5ORF22</td>
<td>5HSAA015007</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA015007/1">UTR</a></td>
<td>URS0000D7CBD6_1519565</td>
<td><a href="https://rnacentral.org/rna/URS0000D7CBD6/1519565">RS</a></td>
<td>2.943</td>
<td>0.07702008</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C5ORF22">=></a></td>
</tr>
<tr>
<td>SLC39A7</td>
<td>5HSAA100275</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA100275/1">UTR</a></td>
<td>URS0000AB4EB2_88036</td>
<td><a href="https://rnacentral.org/rna/URS0000AB4EB2/88036">RS</a></td>
<td>3.81</td>
<td>0.07519954</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SLC39A7">=></a></td>
</tr>
<tr>
<td>RANBP6</td>
<td>5HSAA088578</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA088578/1">UTR</a></td>
<td>URS0000DB41F6_1519565</td>
<td><a href="https://rnacentral.org/rna/URS0000DB41F6/1519565">RS</a></td>
<td>2.6</td>
<td>0.07496591</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RANBP6">=></a></td>
</tr>
<tr>
<td>C1ORF162</td>
<td>5HSAA013652</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA013652/1">UTR</a></td>
<td>URS0000BE2C05_67767</td>
<td><a href="https://rnacentral.org/rna/URS0000BE2C05/67767">RS</a></td>
<td>3.126</td>
<td>0.07448698</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C1ORF162">=></a></td>
</tr>
<tr>
<td>NOP2</td>
<td>5HSAA072816</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072816/1">UTR</a></td>
<td>URS0000C217CE_46433</td>
<td><a href="https://rnacentral.org/rna/URS0000C217CE/46433">RS</a></td>
<td>1.63</td>
<td>0.07404815</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NOP2">=></a></td>
</tr>
<tr>
<td>ENTPD7</td>
<td>5HSAA035635</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035635/1">UTR</a></td>
<td>URS0000DAC929_201502</td>
<td><a href="https://rnacentral.org/rna/URS0000DAC929/201502">RS</a></td>
<td>2.192</td>
<td>0.07389776</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ENTPD7">=></a></td>
</tr>
<tr>
<td>INTS12</td>
<td>5HSAA053277</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA053277/1">UTR</a></td>
<td>URS0000C217CE_46433</td>
<td><a href="https://rnacentral.org/rna/URS0000C217CE/46433">RS</a></td>
<td>2.447</td>
<td>0.07110862</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/INTS12">=></a></td>
</tr>
<tr>
<td>CD53</td>
<td>5HSAA019893</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA019893/1">UTR</a></td>
<td>URS0000AB482B_573729</td>
<td><a href="https://rnacentral.org/rna/URS0000AB482B/573729">RS</a></td>
<td>2.84</td>
<td>0.07081965</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CD53">=></a></td>
</tr>
<tr>
<td>CLGN</td>
<td>5HSAA022634</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA022634/1">UTR</a></td>
<td>URS0000C3867F_128390</td>
<td><a href="https://rnacentral.org/rna/URS0000C3867F/128390">RS</a></td>
<td>2.654</td>
<td>0.07010488</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CLGN">=></a></td>
</tr>
<tr>
<td>PSMB3</td>
<td>5HSAA085510</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085510/1">UTR</a></td>
<td>URS0000C1CCA7_456900</td>
<td><a href="https://rnacentral.org/rna/URS0000C1CCA7/456900">RS</a></td>
<td>3.346</td>
<td>0.06953203</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMB3">=></a></td>
</tr>
<tr>
<td>NEK2</td>
<td>5HSAA071502</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071502/1">UTR</a></td>
<td>URS0000AB9E65_10116</td>
<td><a href="https://rnacentral.org/rna/URS0000AB9E65/10116">RS</a></td>
<td>3.228</td>
<td>0.06780514</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NEK2">=></a></td>
</tr>
<tr>
<td>C11ORF45</td>
<td>5HSAA011892</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA011892/1">UTR</a></td>
<td>URS0000BEE6C0_1367422</td>
<td><a href="https://rnacentral.org/rna/URS0000BEE6C0/1367422">RS</a></td>
<td>3.279</td>
<td>0.06760099</td>
<td><a href="/_mds/c11orf45.md">=></a></td>
</tr>
<tr>
<td>ACTN4</td>
<td>5HSAA001733</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA001733/1">UTR</a></td>
<td>URS0000BE4B63_655819</td>
<td><a href="https://rnacentral.org/rna/URS0000BE4B63/655819">RS</a></td>
<td>2.574</td>
<td>0.06650996</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ACTN4">=></a></td>
</tr>
<tr>
<td>ANAPC10</td>
<td>5HSAA004369</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004369/1">UTR</a></td>
<td>URS0000C556B5_36166</td>
<td><a href="https://rnacentral.org/rna/URS0000C556B5/36166">RS</a></td>
<td>2.656</td>
<td>0.06611948</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/anapc10.md">=></a></td>
</tr>
<tr>
<td>PTPN23</td>
<td>5HSAA086434</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086434/1">UTR</a></td>
<td>URS0000C13939_1104152</td>
<td><a href="https://rnacentral.org/rna/URS0000C13939/1104152">RS</a></td>
<td>3.796</td>
<td>0.06555846</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PTPN23">=></a></td>
</tr>
<tr>
<td>NR1H3</td>
<td>5HSAA073244</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA073244/1">UTR</a></td>
<td>URS0000AB55EC_3988</td>
<td><a href="https://rnacentral.org/rna/URS0000AB55EC/3988">RS</a></td>
<td>1.777</td>
<td>0.06409277</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NR1H3">=></a></td>
</tr>
<tr>
<td>LMO3</td>
<td>5HSAA059436</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059436/1">UTR</a></td>
<td>URS0000BE4540_573508</td>
<td><a href="https://rnacentral.org/rna/URS0000BE4540/573508">RS</a></td>
<td>2.011</td>
<td>0.06398864</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LMO3">=></a></td>
</tr>
<tr>
<td>AMTN</td>
<td>5HSAA004300</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004300/1">UTR</a></td>
<td>URS0000C7D6F3_10181</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D6F3/10181">RS</a></td>
<td>2.607</td>
<td>0.06322051</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AMTN">=></a></td>
</tr>
<tr>
<td>IFI44L</td>
<td>5HSAA051762</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051762/1">UTR</a></td>
<td>URS0000D99040_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000D99040/3562">RS</a></td>
<td>4.95</td>
<td>0.06268307</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IFI44L">=></a></td>
</tr>
<tr>
<td>RPS27A</td>
<td>5HSAA092990</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092990/1">UTR</a></td>
<td>URS0000C501B5_766039</td>
<td><a href="https://rnacentral.org/rna/URS0000C501B5/766039">RS</a></td>
<td>4.585</td>
<td>0.06174005</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS27A">=></a></td>
</tr>
<tr>
<td>CANX</td>
<td>5HSAA016580</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA016580/1">UTR</a></td>
<td>URS0000AB5604_658429</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5604/658429">RS</a></td>
<td>2.258</td>
<td>0.06137698</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CANX">=></a></td>
</tr>
<tr>
<td>SVOP</td>
<td>5HSAA106162</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA106162/1">UTR</a></td>
<td>URS0000DB06EF_1835702</td>
<td><a href="https://rnacentral.org/rna/URS0000DB06EF/1835702">RS</a></td>
<td>4.036</td>
<td>0.05900704</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SVOP">=></a></td>
</tr>
<tr>
<td>UBAP2L</td>
<td>5HSAA115804</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115804/1">UTR</a></td>
<td>URS0000ABB6C6_556484</td>
<td><a href="https://rnacentral.org/rna/URS0000ABB6C6/556484">RS</a></td>
<td>3.875</td>
<td>0.05889315</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBAP2L">=></a></td>
</tr>
<tr>
<td>ATP6AP1L</td>
<td>5HSAA008559</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA008559/1">UTR</a></td>
<td>URS0000C070E4_157072</td>
<td><a href="https://rnacentral.org/rna/URS0000C070E4/157072">RS</a></td>
<td>2.448</td>
<td>0.05871011</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ATP6AP1L">=></a></td>
</tr>
<tr>
<td>GRIK2</td>
<td>5HSAA046732</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA046732/1">UTR</a></td>
<td>URS0000C3AF45_765868</td>
<td><a href="https://rnacentral.org/rna/URS0000C3AF45/765868">RS</a></td>
<td>2.269</td>
<td>0.05695012</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GRIK2">=></a></td>
</tr>
<tr>
<td>TP53RK</td>
<td>5HSAA112670</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA112670/1">UTR</a></td>
<td>URS0000ABAE5D_30025</td>
<td><a href="https://rnacentral.org/rna/URS0000ABAE5D/30025">RS</a></td>
<td>3.48</td>
<td>0.05646029</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TP53RK">=></a></td>
</tr>
<tr>
<td>NPM1</td>
<td>5HSAA073104</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA073104/1">UTR</a></td>
<td>URS0000AB53CF_400682</td>
<td><a href="https://rnacentral.org/rna/URS0000AB53CF/400682">RS</a></td>
<td>2.898</td>
<td>0.0563633</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NPM1">=></a></td>
</tr>
<tr>
<td>MYL12B</td>
<td>5HSAA069209</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA069209/1">UTR</a></td>
<td>URS0000AB3BC4_5454</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3BC4/5454">RS</a></td>
<td>2.707</td>
<td>0.05630592</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MYL12B">=></a></td>
</tr>
<tr>
<td>TBR1</td>
<td>5HSAA107497</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA107497/1">UTR</a></td>
<td>URS0000BE99C8_4572</td>
<td><a href="https://rnacentral.org/rna/URS0000BE99C8/4572">RS</a></td>
<td>3.261</td>
<td>0.05602463</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TBR1">=></a></td>
</tr>
<tr>
<td>PDE6B</td>
<td>5HSAA078297</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA078297/1">UTR</a></td>
<td>URS0000AB421D_331117</td>
<td><a href="https://rnacentral.org/rna/URS0000AB421D/331117">RS</a></td>
<td>3.105</td>
<td>0.05492174</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PDE6B">=></a></td>
</tr>
<tr>
<td>CEP70</td>
<td>5HSAA021115</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA021115/1">UTR</a></td>
<td>URS0000C6B09E_1043005</td>
<td><a href="https://rnacentral.org/rna/URS0000C6B09E/1043005">RS</a></td>
<td>2.071</td>
<td>0.05483266</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CEP70">=></a></td>
</tr>
<tr>
<td>LARP7</td>
<td>5HSAA057962</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057962/1">UTR</a></td>
<td>URS0000D2E3A7_74649</td>
<td><a href="https://rnacentral.org/rna/URS0000D2E3A7/74649">RS</a></td>
<td>3.461</td>
<td>0.0543296</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LARP7">=></a></td>
</tr>
<tr>
<td>KIAA1737</td>
<td>5HSAA056235</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA056235/1">UTR</a></td>
<td>URS0000C1302D_77166</td>
<td><a href="https://rnacentral.org/rna/URS0000C1302D/77166">RS</a></td>
<td>2.662</td>
<td>0.05351575</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KIAA1737">=></a></td>
</tr>
<tr>
<td>HCG_29977</td>
<td>5HSAA048134</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA048134/1">UTR</a></td>
<td>URS0000C2031E_212818</td>
<td><a href="https://rnacentral.org/rna/URS0000C2031E/212818">RS</a></td>
<td>2.457</td>
<td>0.05332911</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HCG_29977">=></a></td>
</tr>
<tr>
<td>UBAP2L</td>
<td>5HSAA115905</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115905/1">UTR</a></td>
<td>URS0000AB6E4A_1245745</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6E4A/1245745">RS</a></td>
<td>2.547</td>
<td>0.05277064</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBAP2L">=></a></td>
</tr>
<tr>
<td>BMX</td>
<td>5HSAA010793</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010793/1">UTR</a></td>
<td>URS0000D8998A_303698</td>
<td><a href="https://rnacentral.org/rna/URS0000D8998A/303698">RS</a></td>
<td>2.372</td>
<td>0.05251203</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BMX">=></a></td>
</tr>
<tr>
<td>KAZALD1</td>
<td>5HSAA054712</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA054712/1">UTR</a></td>
<td>URS0000AB29BB_39946</td>
<td><a href="https://rnacentral.org/rna/URS0000AB29BB/39946">RS</a></td>
<td>2.266</td>
<td>0.05182558</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KAZALD1">=></a></td>
</tr>
<tr>
<td>TMBIM6</td>
<td>5HSAA110059</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA110059/1">UTR</a></td>
<td>URS0000AB3BC4_5454</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3BC4/5454">RS</a></td>
<td>1.881</td>
<td>0.05139971</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMBIM6">=></a></td>
</tr>
</tbody>
</table>