
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
<tr>
<td>USP45</td>
<td>5HSAA117717</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA117717/1">UTR</a></td>
<td>URS0000AB4AB1_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000AB4AB1/12908">RS</a></td>
<td>0.981</td>
<td>0.940</td>
<td>-54.312</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/USP45">=></a></td>
</tr>
<tr>
<td>FGGY</td>
<td>5HSAA040842</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA040842/1">UTR</a></td>
<td>URS0000AB432C_997346</td>
<td><a href="https://rnacentral.org/rna/URS0000AB432C/997346">RS</a></td>
<td>0.962</td>
<td>0.969</td>
<td>-29.315</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FGGY">=></a></td>
</tr>
<tr>
<td>WTAP</td>
<td>5HSAA119986</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA119986/1">UTR</a></td>
<td>URS00021E8189_2772300</td>
<td><a href="https://rnacentral.org/rna/URS00021E8189/2772300">RS</a></td>
<td>0.985</td>
<td>0.942</td>
<td>-39.420</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/WTAP">=></a></td>
</tr>
<tr>
<td>DDX58</td>
<td>5HSAA029348</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029348/1">UTR</a></td>
<td>URS0000E603D5_1642949</td>
<td><a href="https://rnacentral.org/rna/URS0000E603D5/1642949">RS</a></td>
<td>0.965</td>
<td>0.985</td>
<td>-14.984</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DDX58">=></a></td>
</tr>
<tr>
<td>ANAPC10</td>
<td>5HSAA004373</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004373/1">UTR</a></td>
<td>URS00023169CF_1274</td>
<td><a href="https://rnacentral.org/rna/URS00023169CF/1274">RS</a></td>
<td>0.990</td>
<td>0.936</td>
<td>-32.098</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ANAPC10">=></a></td>
</tr>
<tr>
<td>RPL26L1</td>
<td>5HSAA092485</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092485/1">UTR</a></td>
<td>URS0000D7FD1B_362257</td>
<td><a href="https://rnacentral.org/rna/URS0000D7FD1B/362257">RS</a></td>
<td>0.947</td>
<td>0.973</td>
<td>-23.866</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL26L1">=></a></td>
</tr>
<tr>
<td>SEC24D</td>
<td>5HSAA095814</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095814/1">UTR</a></td>
<td>URS00019E0829_192</td>
<td><a href="https://rnacentral.org/rna/URS00019E0829/192">RS</a></td>
<td>0.981</td>
<td>0.958</td>
<td>-29.797</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SEC24D">=></a></td>
</tr>
<tr>
<td>GNL2</td>
<td>5HSAA045356</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA045356/1">UTR</a></td>
<td>URS0000C25A3A_1121305</td>
<td><a href="https://rnacentral.org/rna/URS0000C25A3A/1121305">RS</a></td>
<td>0.990</td>
<td>0.968</td>
<td>-27.331</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GNL2">=></a></td>
</tr>
<tr>
<td>LARP7</td>
<td>5HSAA057965</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057965/1">UTR</a></td>
<td>URS000079623A_1473546</td>
<td><a href="https://rnacentral.org/rna/URS000079623A/1473546">RS</a></td>
<td>0.944</td>
<td>0.961</td>
<td>-22.579</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LARP7">=></a></td>
</tr>
<tr>
<td>HOXC11</td>
<td>5HSAA050596</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050596/1">UTR</a></td>
<td>URS0000C23589_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C23589/12908">RS</a></td>
<td>0.999</td>
<td>0.982</td>
<td>-12.087</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXC11">=></a></td>
</tr>
<tr>
<td>AMTN</td>
<td>5HSAA004299</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004299/1">UTR</a></td>
<td>URS000232A18C_281689</td>
<td><a href="https://rnacentral.org/rna/URS000232A18C/281689">RS</a></td>
<td>0.959</td>
<td>0.964</td>
<td>-18.225</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AMTN">=></a></td>
</tr>
<tr>
<td>ODAM</td>
<td>5HSAA074861</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA074861/1">UTR</a></td>
<td>URS0000D784D0_1502764</td>
<td><a href="https://rnacentral.org/rna/URS0000D784D0/1502764">RS</a></td>
<td>0.961</td>
<td>0.986</td>
<td>-2.449</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ODAM">=></a></td>
</tr>
<tr>
<td>COQ7</td>
<td>5HSAA024360</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024360/1">UTR</a></td>
<td>URS00021EDDE3_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDDE3/12908">RS</a></td>
<td>0.964</td>
<td>0.971</td>
<td>-19.822</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COQ7">=></a></td>
</tr>
<tr>
<td>MAGOHB</td>
<td>5HSAA061975</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA061975/1">UTR</a></td>
<td>URS0000C87674_29311</td>
<td><a href="https://rnacentral.org/rna/URS0000C87674/29311">RS</a></td>
<td>0.987</td>
<td>0.952</td>
<td>-34.595</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAGOHB">=></a></td>
</tr>
<tr>
<td>UNC5D</td>
<td>5HSAA116951</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA116951/1">UTR</a></td>
<td>URS0000C11A2A_1660125</td>
<td><a href="https://rnacentral.org/rna/URS0000C11A2A/1660125">RS</a></td>
<td>0.978</td>
<td>0.981</td>
<td>-14.491</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UNC5D">=></a></td>
</tr>
<tr>
<td>TMEM80</td>
<td>5HSAA111466</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111466/1">UTR</a></td>
<td>URS0000C6EFFE_318464</td>
<td><a href="https://rnacentral.org/rna/URS0000C6EFFE/318464">RS</a></td>
<td>0.964</td>
<td>0.946</td>
<td>-62.102</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMEM80">=></a></td>
</tr>
<tr>
<td>LBR</td>
<td>5HSAA058361</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA058361/1">UTR</a></td>
<td>URS000232B7B9_1122155</td>
<td><a href="https://rnacentral.org/rna/URS000232B7B9/1122155">RS</a></td>
<td>0.987</td>
<td>0.944</td>
<td>-65.994</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LBR">=></a></td>
</tr>
<tr>
<td>TBRG4</td>
<td>5HSAA107535</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA107535/1">UTR</a></td>
<td>URS0000AB3FF2_226900</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3FF2/226900">RS</a></td>
<td>0.969</td>
<td>0.961</td>
<td>-7.848</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TBRG4">=></a></td>
</tr>
<tr>
<td>CCDC138</td>
<td>5HSAA018349</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018349/1">UTR</a></td>
<td>URS00021EE184_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EE184/12908">RS</a></td>
<td>0.972</td>
<td>0.975</td>
<td>-32.992</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC138">=></a></td>
</tr>
<tr>
<td>CLCA4</td>
<td>5HSAA022358</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA022358/1">UTR</a></td>
<td>URS0000DB24FF_1703345</td>
<td><a href="https://rnacentral.org/rna/URS0000DB24FF/1703345">RS</a></td>
<td>0.978</td>
<td>0.983</td>
<td>-11.549</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CLCA4">=></a></td>
</tr>
<tr>
<td>PSMD10</td>
<td>5HSAA085629</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085629/1">UTR</a></td>
<td>URS0002314CE1_32049</td>
<td><a href="https://rnacentral.org/rna/URS0002314CE1/32049">RS</a></td>
<td>0.969</td>
<td>0.950</td>
<td>-45.049</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMD10">=></a></td>
</tr>
<tr>
<td>HMGB1</td>
<td>5HSAA049629</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049629/1">UTR</a></td>
<td>URS0002332872_1230466</td>
<td><a href="https://rnacentral.org/rna/URS0002332872/1230466">RS</a></td>
<td>0.957</td>
<td>0.904</td>
<td>-55.963</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HMGB1">=></a></td>
</tr>
<tr>
<td>RPAP3</td>
<td>5HSAA092262</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092262/1">UTR</a></td>
<td>URS0000C0FFFA_1504672</td>
<td><a href="https://rnacentral.org/rna/URS0000C0FFFA/1504672">RS</a></td>
<td>0.947</td>
<td>0.979</td>
<td>-17.518</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPAP3">=></a></td>
</tr>
<tr>
<td>ACTR6</td>
<td>5HSAA001798</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA001798/1">UTR</a></td>
<td>URS0000C5868E_641107</td>
<td><a href="https://rnacentral.org/rna/URS0000C5868E/641107">RS</a></td>
<td>0.992</td>
<td>0.974</td>
<td>-24.432</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ACTR6">=></a></td>
</tr>
<tr>
<td>RPL26L1</td>
<td>5HSAA092481</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092481/1">UTR</a></td>
<td>URS0000D93F65_1798301</td>
<td><a href="https://rnacentral.org/rna/URS0000D93F65/1798301">RS</a></td>
<td>0.950</td>
<td>0.970</td>
<td>-22.166</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL26L1">=></a></td>
</tr>
<tr>
<td>MRPS10</td>
<td>5HSAA067584</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067584/1">UTR</a></td>
<td>URS0000D6C678_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6C678/12908">RS</a></td>
<td>0.990</td>
<td>0.971</td>
<td>-32.942</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPS10">=></a></td>
</tr>
<tr>
<td>LDHB</td>
<td>5HSAA058545</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA058545/1">UTR</a></td>
<td>URS0000D89FBE_1121391</td>
<td><a href="https://rnacentral.org/rna/URS0000D89FBE/1121391">RS</a></td>
<td>0.992</td>
<td>0.983</td>
<td>-7.670</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LDHB">=></a></td>
</tr>
<tr>
<td>NOSIP</td>
<td>5HSAA072878</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072878/1">UTR</a></td>
<td>URS000231A4EC_1263015</td>
<td><a href="https://rnacentral.org/rna/URS000231A4EC/1263015">RS</a></td>
<td>0.987</td>
<td>0.976</td>
<td>-22.204</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NOSIP">=></a></td>
</tr>
<tr>
<td>PAGE4</td>
<td>5HSAA076250</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA076250/1">UTR</a></td>
<td>URS0000DB57F4_1904970</td>
<td><a href="https://rnacentral.org/rna/URS0000DB57F4/1904970">RS</a></td>
<td>0.974</td>
<td>0.970</td>
<td>-21.391</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PAGE4">=></a></td>
</tr>
<tr>
<td>EXOG</td>
<td>5HSAA037262</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA037262/1">UTR</a></td>
<td>URS0000C6A532_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C6A532/12908">RS</a></td>
<td>0.962</td>
<td>0.986</td>
<td>-10.492</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EXOG">=></a></td>
</tr>
<tr>
<td>HDAC6</td>
<td>5HSAA048213</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA048213/1">UTR</a></td>
<td>URS0000C80E84_1590651</td>
<td><a href="https://rnacentral.org/rna/URS0000C80E84/1590651">RS</a></td>
<td>0.991</td>
<td>0.943</td>
<td>-55.894</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HDAC6">=></a></td>
</tr>
<tr>
<td>KLHL24</td>
<td>5HSAA056955</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA056955/1">UTR</a></td>
<td>URS0000C75E16_1736531</td>
<td><a href="https://rnacentral.org/rna/URS0000C75E16/1736531">RS</a></td>
<td>0.978</td>
<td>0.964</td>
<td>-9.768</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KLHL24">=></a></td>
</tr>
<tr>
<td>RDX</td>
<td>5HSAA089972</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089972/1">UTR</a></td>
<td>URS0000DA404C_1895831</td>
<td><a href="https://rnacentral.org/rna/URS0000DA404C/1895831">RS</a></td>
<td>0.999</td>
<td>0.951</td>
<td>-9.800</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RDX">=></a></td>
</tr>
<tr>
<td>PARP15</td>
<td>5HSAA076800</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA076800/1">UTR</a></td>
<td>URS0000E60876_1801836</td>
<td><a href="https://rnacentral.org/rna/URS0000E60876/1801836">RS</a></td>
<td>0.963</td>
<td>0.984</td>
<td>-8.890</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PARP15">=></a></td>
</tr>
<tr>
<td>DNAJC28</td>
<td>5HSAA031089</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA031089/1">UTR</a></td>
<td>URS0002332643_1262869</td>
<td><a href="https://rnacentral.org/rna/URS0002332643/1262869">RS</a></td>
<td>0.971</td>
<td>0.952</td>
<td>-55.790</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DNAJC28">=></a></td>
</tr>
<tr>
<td>RPS12</td>
<td>5HSAA092848</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092848/1">UTR</a></td>
<td>URS0000D9898D_572036</td>
<td><a href="https://rnacentral.org/rna/URS0000D9898D/572036">RS</a></td>
<td>0.944</td>
<td>0.963</td>
<td>-37.185</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS12">=></a></td>
</tr>
<tr>
<td>TEX12</td>
<td>5HSAA108462</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA108462/1">UTR</a></td>
<td>URS00021EDDA3_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDDA3/12908">RS</a></td>
<td>0.977</td>
<td>0.961</td>
<td>-21.231</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TEX12">=></a></td>
</tr>
<tr>
<td>SNX2</td>
<td>5HSAA102206</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA102206/1">UTR</a></td>
<td>URS0000AB2AD9_700597</td>
<td><a href="https://rnacentral.org/rna/URS0000AB2AD9/700597">RS</a></td>
<td>0.961</td>
<td>0.983</td>
<td>-26.305</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SNX2">=></a></td>
</tr>
<tr>
<td>NUP35</td>
<td>5HSAA074329</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA074329/1">UTR</a></td>
<td>URS0002317459_2018041</td>
<td><a href="https://rnacentral.org/rna/URS0002317459/2018041">RS</a></td>
<td>0.999</td>
<td>0.940</td>
<td>-41.255</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NUP35">=></a></td>
</tr>
<tr>
<td>PPIA</td>
<td>5HSAA083315</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083315/1">UTR</a></td>
<td>URS0000D803BB_1920419</td>
<td><a href="https://rnacentral.org/rna/URS0000D803BB/1920419">RS</a></td>
<td>0.988</td>
<td>0.980</td>
<td>-14.839</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPIA">=></a></td>
</tr>
<tr>
<td>ACSS2</td>
<td>5HSAA001650</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA001650/1">UTR</a></td>
<td>URS0000C55050_87541</td>
<td><a href="https://rnacentral.org/rna/URS0000C55050/87541">RS</a></td>
<td>0.939</td>
<td>0.975</td>
<td>-44.744</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ACSS2">=></a></td>
</tr>
<tr>
<td>MAN1A1</td>
<td>5HSAA062043</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA062043/1">UTR</a></td>
<td>URS0000C6DFF8_1345695</td>
<td><a href="https://rnacentral.org/rna/URS0000C6DFF8/1345695">RS</a></td>
<td>0.987</td>
<td>0.976</td>
<td>-23.418</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAN1A1">=></a></td>
</tr>
<tr>
<td>RPL36A</td>
<td>5HSAA092595</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092595/1">UTR</a></td>
<td>URS0000DA671A_1434842</td>
<td><a href="https://rnacentral.org/rna/URS0000DA671A/1434842">RS</a></td>
<td>0.972</td>
<td>0.967</td>
<td>-26.149</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL36A">=></a></td>
</tr>
<tr>
<td>OS9</td>
<td>5HSAA075339-0</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA075339-0/1">UTR</a></td>
<td>URS0002320AAB_1736393</td>
<td><a href="https://rnacentral.org/rna/URS0002320AAB/1736393">RS</a></td>
<td>0.985</td>
<td>0.973</td>
<td>-30.979</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/OS9">=></a></td>
</tr>
<tr>
<td>MIOS</td>
<td>5HSAA065945</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA065945/1">UTR</a></td>
<td>URS0000D6B542_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6B542/12908">RS</a></td>
<td>0.969</td>
<td>0.971</td>
<td>-14.171</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MIOS">=></a></td>
</tr>
<tr>
<td>PRIM1</td>
<td>5HSAA084404</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA084404/1">UTR</a></td>
<td>URS0000D683B1_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D683B1/12908">RS</a></td>
<td>0.964</td>
<td>0.973</td>
<td>-20.675</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRIM1">=></a></td>
</tr>
<tr>
<td>ZNF292</td>
<td>5HSAA122590</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA122590/1">UTR</a></td>
<td>URS0000C8610A_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C8610A/12908">RS</a></td>
<td>0.992</td>
<td>0.960</td>
<td>-19.491</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF292">=></a></td>
</tr>
<tr>
<td>DDX47</td>
<td>5HSAA029136-1</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029136-1/1">UTR</a></td>
<td>URS00021EDD2A_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDD2A/12908">RS</a></td>
<td>0.983</td>
<td>0.982</td>
<td>-9.696</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DDX47">=></a></td>
</tr>
<tr>
<td>YOD1</td>
<td>5HSAA120770</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA120770/1">UTR</a></td>
<td>URS0000C03490_319795</td>
<td><a href="https://rnacentral.org/rna/URS0000C03490/319795">RS</a></td>
<td>1.000</td>
<td>0.979</td>
<td>-14.756</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/YOD1">=></a></td>
</tr>
<tr>
<td>EXOSC3</td>
<td>5HSAA037306</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA037306/1">UTR</a></td>
<td>URS0000C466F4_582475</td>
<td><a href="https://rnacentral.org/rna/URS0000C466F4/582475">RS</a></td>
<td>0.975</td>
<td>0.978</td>
<td>-18.156</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EXOSC3">=></a></td>
</tr>
<tr>
<td>CLK2</td>
<td>5HSAA022812</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA022812/1">UTR</a></td>
<td>URS0000ABB494_717605</td>
<td><a href="https://rnacentral.org/rna/URS0000ABB494/717605">RS</a></td>
<td>0.985</td>
<td>0.987</td>
<td>-3.038</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CLK2">=></a></td>
</tr>
<tr>
<td>SAMD4A</td>
<td>5HSAA094073</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA094073/1">UTR</a></td>
<td>URS0000C59D56_169760</td>
<td><a href="https://rnacentral.org/rna/URS0000C59D56/169760">RS</a></td>
<td>0.997</td>
<td>0.985</td>
<td>-4.566</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SAMD4A">=></a></td>
</tr>
<tr>
<td>ERGIC2</td>
<td>5HSAA036513</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA036513/1">UTR</a></td>
<td>URS0000BEDB8C_1262813</td>
<td><a href="https://rnacentral.org/rna/URS0000BEDB8C/1262813">RS</a></td>
<td>0.982</td>
<td>0.933</td>
<td>-49.213</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ERGIC2">=></a></td>
</tr>
<tr>
<td>MED25</td>
<td>5HSAA064891</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064891/1">UTR</a></td>
<td>URS0000D7FFFD_1718998</td>
<td><a href="https://rnacentral.org/rna/URS0000D7FFFD/1718998">RS</a></td>
<td>0.956</td>
<td>0.959</td>
<td>-37.125</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED25">=></a></td>
</tr>
<tr>
<td>PAX3</td>
<td>5HSAA077049</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA077049/1">UTR</a></td>
<td>URS0000AB8E22_930946</td>
<td><a href="https://rnacentral.org/rna/URS0000AB8E22/930946">RS</a></td>
<td>0.992</td>
<td>0.957</td>
<td>-24.120</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PAX3">=></a></td>
</tr>
<tr>
<td>LARP7</td>
<td>5HSAA057974</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057974/1">UTR</a></td>
<td>URS0000C51897_457402</td>
<td><a href="https://rnacentral.org/rna/URS0000C51897/457402">RS</a></td>
<td>0.929</td>
<td>0.972</td>
<td>-16.554</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LARP7">=></a></td>
</tr>
<tr>
<td>RNF32</td>
<td>5HSAA091695</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA091695/1">UTR</a></td>
<td>URS0002319162_743525</td>
<td><a href="https://rnacentral.org/rna/URS0002319162/743525">RS</a></td>
<td>0.985</td>
<td>0.955</td>
<td>-25.005</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RNF32">=></a></td>
</tr>
<tr>
<td>CCDC138</td>
<td>5HSAA018350-1</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018350-1/1">UTR</a></td>
<td>URS0000D97DBA_1860101</td>
<td><a href="https://rnacentral.org/rna/URS0000D97DBA/1860101">RS</a></td>
<td>0.984</td>
<td>0.959</td>
<td>-43.593</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC138">=></a></td>
</tr>
<tr>
<td>ERG</td>
<td>5HSAA036507</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA036507/1">UTR</a></td>
<td>URS0000D7C4D9_1965625</td>
<td><a href="https://rnacentral.org/rna/URS0000D7C4D9/1965625">RS</a></td>
<td>0.979</td>
<td>0.947</td>
<td>-16.413</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ERG">=></a></td>
</tr>
<tr>
<td>GLA</td>
<td>5HSAA044277</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA044277/1">UTR</a></td>
<td>URS000232D0A4_74033</td>
<td><a href="https://rnacentral.org/rna/URS000232D0A4/74033">RS</a></td>
<td>1.000</td>
<td>0.945</td>
<td>-36.018</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GLA">=></a></td>
</tr>
<tr>
<td>WDTC1</td>
<td>5HSAA119746</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA119746/1">UTR</a></td>
<td>URS0000AB75AD_742740</td>
<td><a href="https://rnacentral.org/rna/URS0000AB75AD/742740">RS</a></td>
<td>0.967</td>
<td>0.941</td>
<td>-36.112</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/WDTC1">=></a></td>
</tr>
<tr>
<td>RPS24</td>
<td>5HSAA092945</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092945/1">UTR</a></td>
<td>URS0000C29148_1490057</td>
<td><a href="https://rnacentral.org/rna/URS0000C29148/1490057">RS</a></td>
<td>0.960</td>
<td>0.972</td>
<td>-22.420</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS24">=></a></td>
</tr>
<tr>
<td>SLC39A10</td>
<td>5HSAA100204</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA100204/1">UTR</a></td>
<td>URS000232C9FB_657309</td>
<td><a href="https://rnacentral.org/rna/URS000232C9FB/657309">RS</a></td>
<td>0.987</td>
<td>0.939</td>
<td>-51.257</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SLC39A10">=></a></td>
</tr>
<tr>
<td>RBP7</td>
<td>5HSAA089750</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089750/1">UTR</a></td>
<td>URS0000C143EB_1671680</td>
<td><a href="https://rnacentral.org/rna/URS0000C143EB/1671680">RS</a></td>
<td>0.996</td>
<td>0.982</td>
<td>-31.478</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RBP7">=></a></td>
</tr>
<tr>
<td>HBP1</td>
<td>5HSAA048031</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA048031/1">UTR</a></td>
<td>URS0000C5371E_666686</td>
<td><a href="https://rnacentral.org/rna/URS0000C5371E/666686">RS</a></td>
<td>0.972</td>
<td>0.907</td>
<td>-26.485</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HBP1">=></a></td>
</tr>
<tr>
<td>UBAP2L</td>
<td>5HSAA116015</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA116015/1">UTR</a></td>
<td>URS000064C5E1_204773</td>
<td><a href="https://rnacentral.org/rna/URS000064C5E1/204773">RS</a></td>
<td>0.962</td>
<td>0.939</td>
<td>-56.926</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBAP2L">=></a></td>
</tr>
<tr>
<td>AMTN</td>
<td>5HSAA004300</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004300/1">UTR</a></td>
<td>URS0000AB44C1_650150</td>
<td><a href="https://rnacentral.org/rna/URS0000AB44C1/650150">RS</a></td>
<td>0.971</td>
<td>0.958</td>
<td>-21.218</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AMTN">=></a></td>
</tr>
<tr>
<td>OPCML</td>
<td>5HSAA075140</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA075140/1">UTR</a></td>
<td>URS00021EDCB7_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDCB7/12908">RS</a></td>
<td>0.988</td>
<td>0.976</td>
<td>-8.642</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/OPCML">=></a></td>
</tr>
<tr>
<td>FAM114A2</td>
<td>5HSAA037797</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA037797/1">UTR</a></td>
<td>URS0000C5072F_1792508</td>
<td><a href="https://rnacentral.org/rna/URS0000C5072F/1792508">RS</a></td>
<td>0.960</td>
<td>0.952</td>
<td>-44.460</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FAM114A2">=></a></td>
</tr>
<tr>
<td>ZNF611</td>
<td>5HSAA123523</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123523/1">UTR</a></td>
<td>URS0000C6EAC8_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C6EAC8/12908">RS</a></td>
<td>0.997</td>
<td>0.965</td>
<td>-21.191</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF611">=></a></td>
</tr>
<tr>
<td>TTF1</td>
<td>5HSAA114867</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114867/1">UTR</a></td>
<td>URS000232F752_1619947</td>
<td><a href="https://rnacentral.org/rna/URS000232F752/1619947">RS</a></td>
<td>0.959</td>
<td>0.961</td>
<td>-17.781</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TTF1">=></a></td>
</tr>
<tr>
<td>MAD2L2</td>
<td>5HSAA061402</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA061402/1">UTR</a></td>
<td>URS0000AB61AB_398511</td>
<td><a href="https://rnacentral.org/rna/URS0000AB61AB/398511">RS</a></td>
<td>0.985</td>
<td>0.968</td>
<td>-49.399</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAD2L2">=></a></td>
</tr>
<tr>
<td>MRPL54</td>
<td>5HSAA067554</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067554/1">UTR</a></td>
<td>URS0000C33663_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C33663/12908">RS</a></td>
<td>0.997</td>
<td>0.981</td>
<td>-12.451</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPL54">=></a></td>
</tr>
<tr>
<td>SPIRE1</td>
<td>5HSAA103380</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103380/1">UTR</a></td>
<td>URS0000C894A6_709839</td>
<td><a href="https://rnacentral.org/rna/URS0000C894A6/709839">RS</a></td>
<td>0.980</td>
<td>0.965</td>
<td>-22.133</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPIRE1">=></a></td>
</tr>
<tr>
<td>RSRC1</td>
<td>5HSAA093492</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093492/1">UTR</a></td>
<td>URS0002331CDB_1609133</td>
<td><a href="https://rnacentral.org/rna/URS0002331CDB/1609133">RS</a></td>
<td>0.976</td>
<td>0.959</td>
<td>-35.154</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RSRC1">=></a></td>
</tr>
<tr>
<td>RPL10</td>
<td>5HSAA092342</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092342/1">UTR</a></td>
<td>URS0000C60B12_1789224</td>
<td><a href="https://rnacentral.org/rna/URS0000C60B12/1789224">RS</a></td>
<td>0.990</td>
<td>0.983</td>
<td>-19.729</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL10">=></a></td>
</tr>
<tr>
<td>PUS7L</td>
<td>5HSAA086864</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086864/1">UTR</a></td>
<td>URS0000ABC521_335541</td>
<td><a href="https://rnacentral.org/rna/URS0000ABC521/335541">RS</a></td>
<td>0.963</td>
<td>0.913</td>
<td>-57.728</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PUS7L">=></a></td>
</tr>
<tr>
<td>ROCK2</td>
<td>5HSAA092039</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092039/1">UTR</a></td>
<td>URS0000D9673B_1507870</td>
<td><a href="https://rnacentral.org/rna/URS0000D9673B/1507870">RS</a></td>
<td>0.965</td>
<td>0.924</td>
<td>-31.794</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ROCK2">=></a></td>
</tr>
<tr>
<td>MAP2K4</td>
<td>5HSAA062297</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA062297/1">UTR</a></td>
<td>URS0000D6C268_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6C268/12908">RS</a></td>
<td>0.987</td>
<td>0.977</td>
<td>-20.567</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAP2K4">=></a></td>
</tr>
<tr>
<td>GABRA2</td>
<td>5HSAA042615</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA042615/1">UTR</a></td>
<td>URS00023155ED_1978765</td>
<td><a href="https://rnacentral.org/rna/URS00023155ED/1978765">RS</a></td>
<td>0.962</td>
<td>0.931</td>
<td>-43.779</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GABRA2">=></a></td>
</tr>
<tr>
<td>SPAG11B</td>
<td>5HSAA102737</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA102737/1">UTR</a></td>
<td>URS00021EE11C_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EE11C/12908">RS</a></td>
<td>0.990</td>
<td>0.980</td>
<td>-24.070</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPAG11B">=></a></td>
</tr>
<tr>
<td>TNNI3K</td>
<td>5HSAA112083</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA112083/1">UTR</a></td>
<td>URS0000C38ABC_1455</td>
<td><a href="https://rnacentral.org/rna/URS0000C38ABC/1455">RS</a></td>
<td>0.941</td>
<td>0.983</td>
<td>-5.137</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TNNI3K">=></a></td>
</tr>
<tr>
<td>SRC</td>
<td>5HSAA103797</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103797/1">UTR</a></td>
<td>URS0000DA7627_1817879</td>
<td><a href="https://rnacentral.org/rna/URS0000DA7627/1817879">RS</a></td>
<td>0.955</td>
<td>0.986</td>
<td>-18.016</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SRC">=></a></td>
</tr>
<tr>
<td>RORA</td>
<td>5HSAA092111</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092111/1">UTR</a></td>
<td>URS0000BBD302_1655543</td>
<td><a href="https://rnacentral.org/rna/URS0000BBD302/1655543">RS</a></td>
<td>0.964</td>
<td>0.971</td>
<td>-16.708</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RORA">=></a></td>
</tr>
<tr>
<td>HNF4G</td>
<td>5HSAA049817</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049817/1">UTR</a></td>
<td>URS0000C4EDEC_1666916</td>
<td><a href="https://rnacentral.org/rna/URS0000C4EDEC/1666916">RS</a></td>
<td>0.967</td>
<td>0.990</td>
<td>-11.829</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HNF4G">=></a></td>
</tr>
<tr>
<td>UTP15</td>
<td>5HSAA117897</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA117897/1">UTR</a></td>
<td>URS0002317608_234267</td>
<td><a href="https://rnacentral.org/rna/URS0002317608/234267">RS</a></td>
<td>0.972</td>
<td>0.938</td>
<td>-40.149</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UTP15">=></a></td>
</tr>
<tr>
<td>PRIM1</td>
<td>5HSAA084405</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA084405/1">UTR</a></td>
<td>URS0000C72FB0_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C72FB0/12908">RS</a></td>
<td>0.977</td>
<td>0.985</td>
<td>-13.844</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRIM1">=></a></td>
</tr>
<tr>
<td>HAO1</td>
<td>5HSAA047817</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047817/1">UTR</a></td>
<td>URS0000C5CFFA_1549812</td>
<td><a href="https://rnacentral.org/rna/URS0000C5CFFA/1549812">RS</a></td>
<td>0.976</td>
<td>0.948</td>
<td>-16.298</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HAO1">=></a></td>
</tr>
<tr>
<td>ARHGDIA</td>
<td>5HSAA006309</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA006309/1">UTR</a></td>
<td>URS0000C4A6B2_1794906</td>
<td><a href="https://rnacentral.org/rna/URS0000C4A6B2/1794906">RS</a></td>
<td>0.970</td>
<td>0.956</td>
<td>-42.512</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ARHGDIA">=></a></td>
</tr>
<tr>
<td>XRCC4</td>
<td>5HSAA120460</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA120460/1">UTR</a></td>
<td>URS0000C5A066_1450761</td>
<td><a href="https://rnacentral.org/rna/URS0000C5A066/1450761">RS</a></td>
<td>0.950</td>
<td>0.937</td>
<td>-34.424</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/XRCC4">=></a></td>
</tr>
<tr>
<td>MAPRE1</td>
<td>5HSAA063479</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA063479/1">UTR</a></td>
<td>URS0002328847_1802354</td>
<td><a href="https://rnacentral.org/rna/URS0002328847/1802354">RS</a></td>
<td>0.989</td>
<td>0.919</td>
<td>-58.246</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAPRE1">=></a></td>
</tr>
<tr>
<td>PPIH</td>
<td>5HSAA083355</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083355/1">UTR</a></td>
<td>URS0000ABC7DE_525371</td>
<td><a href="https://rnacentral.org/rna/URS0000ABC7DE/525371">RS</a></td>
<td>0.994</td>
<td>0.970</td>
<td>-36.141</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPIH">=></a></td>
</tr>
<tr>
<td>DFFA</td>
<td>5HSAA029712</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029712/1">UTR</a></td>
<td>URS0002335090_1137096</td>
<td><a href="https://rnacentral.org/rna/URS0002335090/1137096">RS</a></td>
<td>0.956</td>
<td>0.943</td>
<td>-62.001</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DFFA">=></a></td>
</tr>
<tr>
<td>GLA</td>
<td>5HSAA044278</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA044278/1">UTR</a></td>
<td>URS0000E601A3_110319</td>
<td><a href="https://rnacentral.org/rna/URS0000E601A3/110319">RS</a></td>
<td>0.986</td>
<td>0.919</td>
<td>-71.240</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GLA">=></a></td>
</tr>
<tr>
<td>PUS7L</td>
<td>5HSAA086861</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086861/1">UTR</a></td>
<td>URS0000DB0CD0_1090615</td>
<td><a href="https://rnacentral.org/rna/URS0000DB0CD0/1090615">RS</a></td>
<td>0.931</td>
<td>0.971</td>
<td>-15.122</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PUS7L">=></a></td>
</tr>
<tr>
<td>FGF14</td>
<td>5HSAA040628</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA040628/1">UTR</a></td>
<td>URS000231C6F0_37928</td>
<td><a href="https://rnacentral.org/rna/URS000231C6F0/37928">RS</a></td>
<td>0.991</td>
<td>0.961</td>
<td>-25.837</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FGF14">=></a></td>
</tr>
<tr>
<td>CCDC127</td>
<td>5HSAA018290</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018290/1">UTR</a></td>
<td>URS000232B1DE_1432141</td>
<td><a href="https://rnacentral.org/rna/URS000232B1DE/1432141">RS</a></td>
<td>0.997</td>
<td>0.962</td>
<td>-40.376</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC127">=></a></td>
</tr>
<tr>
<td>SCYL2</td>
<td>5HSAA095308</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095308/1">UTR</a></td>
<td>URS0000BF1F3D_481448</td>
<td><a href="https://rnacentral.org/rna/URS0000BF1F3D/481448">RS</a></td>
<td>0.987</td>
<td>0.978</td>
<td>-16.357</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SCYL2">=></a></td>
</tr>
<tr>
<td>KIF18A</td>
<td>5HSAA056345</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA056345/1">UTR</a></td>
<td>URS0000D95B11_1954209</td>
<td><a href="https://rnacentral.org/rna/URS0000D95B11/1954209">RS</a></td>
<td>0.968</td>
<td>0.926</td>
<td>-27.705</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KIF18A">=></a></td>
</tr>
<tr>
<td>NDUFA2</td>
<td>5HSAA071169</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071169/1">UTR</a></td>
<td>URS0000C4FD18_1223543</td>
<td><a href="https://rnacentral.org/rna/URS0000C4FD18/1223543">RS</a></td>
<td>0.991</td>
<td>0.963</td>
<td>-26.732</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NDUFA2">=></a></td>
</tr>
<tr>
<td>RRH</td>
<td>5HSAA093324</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093324/1">UTR</a></td>
<td>URS0000D6D026_349102</td>
<td><a href="https://rnacentral.org/rna/URS0000D6D026/349102">RS</a></td>
<td>0.977</td>
<td>0.965</td>
<td>-8.482</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RRH">=></a></td>
</tr>
<tr>
<td>KIAA1143</td>
<td>5HSAA055966</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA055966/1">UTR</a></td>
<td>URS00021EDCDD_391613</td>
<td><a href="https://rnacentral.org/rna/URS00021EDCDD/391613">RS</a></td>
<td>0.961</td>
<td>0.979</td>
<td>-4.282</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KIAA1143">=></a></td>
</tr>
<tr>
<td>ERP27</td>
<td>5HSAA036688</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA036688/1">UTR</a></td>
<td>URS0000C17FDC_1226325</td>
<td><a href="https://rnacentral.org/rna/URS0000C17FDC/1226325">RS</a></td>
<td>0.967</td>
<td>0.939</td>
<td>-41.924</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ERP27">=></a></td>
</tr>
<tr>
<td>AFP</td>
<td>5HSAA002803</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA002803/1">UTR</a></td>
<td>URS0000D7B5A7_1121025</td>
<td><a href="https://rnacentral.org/rna/URS0000D7B5A7/1121025">RS</a></td>
<td>0.952</td>
<td>0.962</td>
<td>-23.682</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AFP">=></a></td>
</tr>
<tr>
<td>NONO</td>
<td>5HSAA072788</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072788/1">UTR</a></td>
<td>URS00023334EC_98228</td>
<td><a href="https://rnacentral.org/rna/URS00023334EC/98228">RS</a></td>
<td>0.962</td>
<td>0.950</td>
<td>-60.476</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NONO">=></a></td>
</tr>
<tr>
<td>BMI1</td>
<td>5HSAA010719</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010719/1">UTR</a></td>
<td>URS0000AB37DD_350688</td>
<td><a href="https://rnacentral.org/rna/URS0000AB37DD/350688">RS</a></td>
<td>0.955</td>
<td>0.974</td>
<td>-29.244</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BMI1">=></a></td>
</tr>
<tr>
<td>EPB41L3</td>
<td>5HSAA035760</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035760/1">UTR</a></td>
<td>URS0000C578E0_1121326</td>
<td><a href="https://rnacentral.org/rna/URS0000C578E0/1121326">RS</a></td>
<td>0.982</td>
<td>0.972</td>
<td>-11.838</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EPB41L3">=></a></td>
</tr>
<tr>
<td>C1D</td>
<td>5HSAA013480</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA013480/1">UTR</a></td>
<td>URS0000BEE0C1_330214</td>
<td><a href="https://rnacentral.org/rna/URS0000BEE0C1/330214">RS</a></td>
<td>0.962</td>
<td>0.980</td>
<td>-18.536</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C1D">=></a></td>
</tr>
<tr>
<td>SMC4</td>
<td>5HSAA101368</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101368/1">UTR</a></td>
<td>URS0000DAA856_1881045</td>
<td><a href="https://rnacentral.org/rna/URS0000DAA856/1881045">RS</a></td>
<td>0.992</td>
<td>0.950</td>
<td>-28.195</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SMC4">=></a></td>
</tr>
<tr>
<td>SRGAP1</td>
<td>5HSAA103832</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103832/1">UTR</a></td>
<td>URS0000D965CF_1889883</td>
<td><a href="https://rnacentral.org/rna/URS0000D965CF/1889883">RS</a></td>
<td>0.986</td>
<td>0.957</td>
<td>-10.719</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SRGAP1">=></a></td>
</tr>
<tr>
<td>RPL12</td>
<td>5HSAA092362</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092362/1">UTR</a></td>
<td>URS0000AB3D0B_568816</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3D0B/568816">RS</a></td>
<td>0.981</td>
<td>0.959</td>
<td>-43.195</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL12">=></a></td>
</tr>
<tr>
<td>RUVBL2</td>
<td>5HSAA093763</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093763/1">UTR</a></td>
<td>URS0000C7BA37_1679168</td>
<td><a href="https://rnacentral.org/rna/URS0000C7BA37/1679168">RS</a></td>
<td>0.973</td>
<td>0.984</td>
<td>-6.849</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RUVBL2">=></a></td>
</tr>
<tr>
<td>SUB1</td>
<td>5HSAA105736</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA105736/1">UTR</a></td>
<td>URS000231873E_1075090</td>
<td><a href="https://rnacentral.org/rna/URS000231873E/1075090">RS</a></td>
<td>1.000</td>
<td>0.970</td>
<td>-16.884</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SUB1">=></a></td>
</tr>
<tr>
<td>EPHA7</td>
<td>5HSAA036090</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA036090/1">UTR</a></td>
<td>URS00023267CB_1431546</td>
<td><a href="https://rnacentral.org/rna/URS00023267CB/1431546">RS</a></td>
<td>0.962</td>
<td>0.898</td>
<td>-57.927</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EPHA7">=></a></td>
</tr>
<tr>
<td>E2F5</td>
<td>5HSAA032963</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA032963/1">UTR</a></td>
<td>URS0000D697B5_311403</td>
<td><a href="https://rnacentral.org/rna/URS0000D697B5/311403">RS</a></td>
<td>1.000</td>
<td>0.990</td>
<td>-17.801</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/E2F5">=></a></td>
</tr>
<tr>
<td>NCAPG2</td>
<td>5HSAA070418</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA070418/1">UTR</a></td>
<td>URS0000D8F631_1121331</td>
<td><a href="https://rnacentral.org/rna/URS0000D8F631/1121331">RS</a></td>
<td>0.982</td>
<td>0.925</td>
<td>-58.767</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NCAPG2">=></a></td>
</tr>
<tr>
<td>POP4</td>
<td>5HSAA082757</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA082757/1">UTR</a></td>
<td>URS0000C614E0_1523417</td>
<td><a href="https://rnacentral.org/rna/URS0000C614E0/1523417">RS</a></td>
<td>0.937</td>
<td>0.964</td>
<td>-25.957</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/POP4">=></a></td>
</tr>
<tr>
<td>ARID5B</td>
<td>5HSAA006588</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA006588/1">UTR</a></td>
<td>URS0000D65CB2_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D65CB2/12908">RS</a></td>
<td>0.978</td>
<td>0.980</td>
<td>-6.880</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ARID5B">=></a></td>
</tr>
<tr>
<td>TNFRSF13B</td>
<td>5HSAA111882</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111882/1">UTR</a></td>
<td>URS0000D66BD7_1193146</td>
<td><a href="https://rnacentral.org/rna/URS0000D66BD7/1193146">RS</a></td>
<td>0.990</td>
<td>0.977</td>
<td>-12.838</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TNFRSF13B">=></a></td>
</tr>
<tr>
<td>NDUFB8</td>
<td>5HSAA071271</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071271/1">UTR</a></td>
<td>URS0000D9E0F8_1121322</td>
<td><a href="https://rnacentral.org/rna/URS0000D9E0F8/1121322">RS</a></td>
<td>0.984</td>
<td>0.975</td>
<td>-37.495</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NDUFB8">=></a></td>
</tr>
<tr>
<td>TNNI3K</td>
<td>5HSAA112082</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA112082/1">UTR</a></td>
<td>URS0000C73819_943816</td>
<td><a href="https://rnacentral.org/rna/URS0000C73819/943816">RS</a></td>
<td>0.971</td>
<td>0.977</td>
<td>-7.003</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TNNI3K">=></a></td>
</tr>
<tr>
<td>SEC23IP</td>
<td>5HSAA095764</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095764/1">UTR</a></td>
<td>URS0000ABC069_408172</td>
<td><a href="https://rnacentral.org/rna/URS0000ABC069/408172">RS</a></td>
<td>1.000</td>
<td>0.971</td>
<td>-38.812</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SEC23IP">=></a></td>
</tr>
<tr>
<td>GSS</td>
<td>5HSAA047016</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047016/1">UTR</a></td>
<td>URS0000DAE2CF_1895849</td>
<td><a href="https://rnacentral.org/rna/URS0000DAE2CF/1895849">RS</a></td>
<td>0.962</td>
<td>0.964</td>
<td>-41.741</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GSS">=></a></td>
</tr>
<tr>
<td>HMGB1</td>
<td>5HSAA049620</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049620/1">UTR</a></td>
<td>URS0000C50408_1351755</td>
<td><a href="https://rnacentral.org/rna/URS0000C50408/1351755">RS</a></td>
<td>0.997</td>
<td>0.957</td>
<td>-43.746</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HMGB1">=></a></td>
</tr>
<tr>
<td>E2F5</td>
<td>5HSAA032962</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA032962/1">UTR</a></td>
<td>URS00008FED37_32046</td>
<td><a href="https://rnacentral.org/rna/URS00008FED37/32046">RS</a></td>
<td>1.000</td>
<td>0.988</td>
<td>-20.679</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/E2F5">=></a></td>
</tr>
<tr>
<td>ZNF687</td>
<td>5HSAA123710</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123710/1">UTR</a></td>
<td>URS00021EDCA5_1305735</td>
<td><a href="https://rnacentral.org/rna/URS00021EDCA5/1305735">RS</a></td>
<td>0.979</td>
<td>0.977</td>
<td>-10.979</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF687">=></a></td>
</tr>
<tr>
<td>CFHR3</td>
<td>5HSAA021321</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA021321/1">UTR</a></td>
<td>URS0000ABB3E8_715226</td>
<td><a href="https://rnacentral.org/rna/URS0000ABB3E8/715226">RS</a></td>
<td>0.973</td>
<td>0.960</td>
<td>-14.925</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CFHR3">=></a></td>
</tr>
<tr>
<td>NDUFA9</td>
<td>5HSAA071201</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071201/1">UTR</a></td>
<td>URS0000C712A8_1697053</td>
<td><a href="https://rnacentral.org/rna/URS0000C712A8/1697053">RS</a></td>
<td>0.932</td>
<td>0.959</td>
<td>-21.314</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NDUFA9">=></a></td>
</tr>
<tr>
<td>ZNF821</td>
<td>5HSAA123998</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123998/1">UTR</a></td>
<td>URS0000AB61FD_1290391</td>
<td><a href="https://rnacentral.org/rna/URS0000AB61FD/1290391">RS</a></td>
<td>0.933</td>
<td>0.925</td>
<td>-33.040</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF821">=></a></td>
</tr>
<tr>
<td>FBXO25</td>
<td>5HSAA039808</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039808/1">UTR</a></td>
<td>URS0000C6BFB4_1221996</td>
<td><a href="https://rnacentral.org/rna/URS0000C6BFB4/1221996">RS</a></td>
<td>0.999</td>
<td>0.964</td>
<td>-29.102</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FBXO25">=></a></td>
</tr>
<tr>
<td>NUSAP1</td>
<td>5HSAA074556</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA074556/1">UTR</a></td>
<td>URS0000AB1FF0_164757</td>
<td><a href="https://rnacentral.org/rna/URS0000AB1FF0/164757">RS</a></td>
<td>0.999</td>
<td>0.958</td>
<td>-30.570</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NUSAP1">=></a></td>
</tr>
<tr>
<td>UBAP2</td>
<td>5HSAA115795</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115795/1">UTR</a></td>
<td>URS0000C066D8_561184</td>
<td><a href="https://rnacentral.org/rna/URS0000C066D8/561184">RS</a></td>
<td>0.933</td>
<td>0.941</td>
<td>-37.659</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBAP2">=></a></td>
</tr>
<tr>
<td>GEM</td>
<td>5HSAA043805</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA043805/1">UTR</a></td>
<td>URS0000AB3759_1088868</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3759/1088868">RS</a></td>
<td>0.973</td>
<td>0.934</td>
<td>-55.416</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GEM">=></a></td>
</tr>
<tr>
<td>PICALM</td>
<td>5HSAA080133</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080133/1">UTR</a></td>
<td>URS0000C4B34E_765913</td>
<td><a href="https://rnacentral.org/rna/URS0000C4B34E/765913">RS</a></td>
<td>0.965</td>
<td>0.944</td>
<td>-47.452</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PICALM">=></a></td>
</tr>
<tr>
<td>NAP1L4</td>
<td>5HSAA069999</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA069999/1">UTR</a></td>
<td>URS0000C106FD_317936</td>
<td><a href="https://rnacentral.org/rna/URS0000C106FD/317936">RS</a></td>
<td>0.949</td>
<td>0.965</td>
<td>-23.843</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NAP1L4">=></a></td>
</tr>
<tr>
<td>OSGEPL1</td>
<td>5HSAA075588</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA075588/1">UTR</a></td>
<td>URS0000D79489_1920420</td>
<td><a href="https://rnacentral.org/rna/URS0000D79489/1920420">RS</a></td>
<td>0.989</td>
<td>0.922</td>
<td>-22.662</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/OSGEPL1">=></a></td>
</tr>
<tr>
<td>AGTPBP1</td>
<td>5HSAA003039</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA003039/1">UTR</a></td>
<td>URS0000C2E9B4_1736490</td>
<td><a href="https://rnacentral.org/rna/URS0000C2E9B4/1736490">RS</a></td>
<td>0.979</td>
<td>0.960</td>
<td>-23.281</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AGTPBP1">=></a></td>
</tr>
<tr>
<td>SPCS3</td>
<td>5HSAA103223</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103223/1">UTR</a></td>
<td>URS00007E186F_611301</td>
<td><a href="https://rnacentral.org/rna/URS00007E186F/611301">RS</a></td>
<td>0.968</td>
<td>0.959</td>
<td>-52.788</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPCS3">=></a></td>
</tr>
<tr>
<td>KDELR3</td>
<td>5HSAA055147</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA055147/1">UTR</a></td>
<td>URS0000BFE0AB_1393034</td>
<td><a href="https://rnacentral.org/rna/URS0000BFE0AB/1393034">RS</a></td>
<td>0.951</td>
<td>0.924</td>
<td>-36.613</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KDELR3">=></a></td>
</tr>
<tr>
<td>HTATIP2</td>
<td>5HSAA051283</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051283/1">UTR</a></td>
<td>URS0000AB2D24_1002672</td>
<td><a href="https://rnacentral.org/rna/URS0000AB2D24/1002672">RS</a></td>
<td>0.929</td>
<td>0.980</td>
<td>-43.163</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HTATIP2">=></a></td>
</tr>
<tr>
<td>DHDH</td>
<td>5HSAA029986</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029986/1">UTR</a></td>
<td>URS0000DB087C_1805364</td>
<td><a href="https://rnacentral.org/rna/URS0000DB087C/1805364">RS</a></td>
<td>0.961</td>
<td>0.970</td>
<td>-21.492</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DHDH">=></a></td>
</tr>
<tr>
<td>LSM8</td>
<td>5HSAA060921</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA060921/1">UTR</a></td>
<td>URS0000D6ABD2_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6ABD2/12908">RS</a></td>
<td>0.983</td>
<td>0.974</td>
<td>-28.081</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LSM8">=></a></td>
</tr>
<tr>
<td>LINGO2</td>
<td>5HSAA059119</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059119/1">UTR</a></td>
<td>URS0000D8E9DF_623280</td>
<td><a href="https://rnacentral.org/rna/URS0000D8E9DF/623280">RS</a></td>
<td>0.961</td>
<td>0.965</td>
<td>-22.394</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LINGO2">=></a></td>
</tr>
<tr>
<td>MRPL22</td>
<td>5HSAA067411</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067411/1">UTR</a></td>
<td>URS0000AB9B31_553207</td>
<td><a href="https://rnacentral.org/rna/URS0000AB9B31/553207">RS</a></td>
<td>0.962</td>
<td>0.920</td>
<td>-39.225</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPL22">=></a></td>
</tr>
<tr>
<td>MOSPD2</td>
<td>5HSAA066969</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA066969/1">UTR</a></td>
<td>URS0000DAA6CF_411959</td>
<td><a href="https://rnacentral.org/rna/URS0000DAA6CF/411959">RS</a></td>
<td>0.977</td>
<td>0.930</td>
<td>-41.761</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MOSPD2">=></a></td>
</tr>
<tr>
<td>RICTOR</td>
<td>5HSAA091018</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA091018/1">UTR</a></td>
<td>URS00021EDB13_195105</td>
<td><a href="https://rnacentral.org/rna/URS00021EDB13/195105">RS</a></td>
<td>1.000</td>
<td>0.982</td>
<td>-17.899</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RICTOR">=></a></td>
</tr>
<tr>
<td>TPRG1L</td>
<td>5HSAA113038</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA113038/1">UTR</a></td>
<td>URS0000C40643_1843690</td>
<td><a href="https://rnacentral.org/rna/URS0000C40643/1843690">RS</a></td>
<td>0.954</td>
<td>0.967</td>
<td>-48.812</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TPRG1L">=></a></td>
</tr>
<tr>
<td>ZNF808</td>
<td>5HSAA123978</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123978/1">UTR</a></td>
<td>URS0000D88E96_692418</td>
<td><a href="https://rnacentral.org/rna/URS0000D88E96/692418">RS</a></td>
<td>0.994</td>
<td>0.941</td>
<td>-27.083</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF808">=></a></td>
</tr>
<tr>
<td>ZNF780A</td>
<td>5HSAA123917</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123917/1">UTR</a></td>
<td>URS0000C39FD2_84024</td>
<td><a href="https://rnacentral.org/rna/URS0000C39FD2/84024">RS</a></td>
<td>0.971</td>
<td>0.972</td>
<td>-23.334</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF780A">=></a></td>
</tr>
<tr>
<td>MED6</td>
<td>5HSAA064928</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064928/1">UTR</a></td>
<td>URS00023309FD_1802031</td>
<td><a href="https://rnacentral.org/rna/URS00023309FD/1802031">RS</a></td>
<td>0.990</td>
<td>0.974</td>
<td>-17.562</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED6">=></a></td>
</tr>
<tr>
<td>DDX41</td>
<td>5HSAA029108</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029108/1">UTR</a></td>
<td>URS0000DA1169_1839759</td>
<td><a href="https://rnacentral.org/rna/URS0000DA1169/1839759">RS</a></td>
<td>0.975</td>
<td>0.971</td>
<td>-26.291</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DDX41">=></a></td>
</tr>
<tr>
<td>ZNF415</td>
<td>5HSAA122929</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA122929/1">UTR</a></td>
<td>URS0000C4338E_1157490</td>
<td><a href="https://rnacentral.org/rna/URS0000C4338E/1157490">RS</a></td>
<td>0.973</td>
<td>0.952</td>
<td>-34.935</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF415">=></a></td>
</tr>
<tr>
<td>BZW1</td>
<td>5HSAA011520</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA011520/1">UTR</a></td>
<td>URS0000DAED74_1986784</td>
<td><a href="https://rnacentral.org/rna/URS0000DAED74/1986784">RS</a></td>
<td>0.960</td>
<td>0.977</td>
<td>-22.222</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BZW1">=></a></td>
</tr>
<tr>
<td>RPS27</td>
<td>5HSAA092984</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092984/1">UTR</a></td>
<td>URS0000E60030_515897</td>
<td><a href="https://rnacentral.org/rna/URS0000E60030/515897">RS</a></td>
<td>0.980</td>
<td>0.982</td>
<td>-13.381</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS27">=></a></td>
</tr>
<tr>
<td>FADS1</td>
<td>5HSAA037588</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA037588/1">UTR</a></td>
<td>URS0000AB2EBF_446469</td>
<td><a href="https://rnacentral.org/rna/URS0000AB2EBF/446469">RS</a></td>
<td>0.988</td>
<td>0.963</td>
<td>-44.948</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FADS1">=></a></td>
</tr>
<tr>
<td>MEIG1</td>
<td>5HSAA064999</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064999/1">UTR</a></td>
<td>URS0002313E0C_47853</td>
<td><a href="https://rnacentral.org/rna/URS0002313E0C/47853">RS</a></td>
<td>0.992</td>
<td>0.948</td>
<td>-47.516</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MEIG1">=></a></td>
</tr>
<tr>
<td>CORO7</td>
<td>5HSAA024467</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024467/1">UTR</a></td>
<td>URS0000C735CB_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C735CB/12908">RS</a></td>
<td>0.988</td>
<td>0.984</td>
<td>-10.944</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CORO7">=></a></td>
</tr>
<tr>
<td>ENPP2</td>
<td>5HSAA035557</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035557/1">UTR</a></td>
<td>URS0000D92503_1827376</td>
<td><a href="https://rnacentral.org/rna/URS0000D92503/1827376">RS</a></td>
<td>0.978</td>
<td>0.965</td>
<td>-24.516</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ENPP2">=></a></td>
</tr>
<tr>
<td>SLC6A3</td>
<td>5HSAA100651</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA100651/1">UTR</a></td>
<td>URS0000C71FA5_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C71FA5/12908">RS</a></td>
<td>0.975</td>
<td>0.984</td>
<td>-9.915</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SLC6A3">=></a></td>
</tr>
<tr>
<td>CCDC73</td>
<td>5HSAA018632</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018632/1">UTR</a></td>
<td>URS0000AB5E57_637616</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5E57/637616">RS</a></td>
<td>0.995</td>
<td>0.971</td>
<td>-9.889</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC73">=></a></td>
</tr>
<tr>
<td>PYROXD1</td>
<td>5HSAA087076</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA087076/1">UTR</a></td>
<td>URS0000C28596_1869</td>
<td><a href="https://rnacentral.org/rna/URS0000C28596/1869">RS</a></td>
<td>0.947</td>
<td>0.979</td>
<td>-24.757</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PYROXD1">=></a></td>
</tr>
<tr>
<td>SNCAIP</td>
<td>5HSAA101875</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101875/1">UTR</a></td>
<td>URS0002329499_1797787</td>
<td><a href="https://rnacentral.org/rna/URS0002329499/1797787">RS</a></td>
<td>0.992</td>
<td>0.948</td>
<td>-23.097</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SNCAIP">=></a></td>
</tr>
<tr>
<td>HMGB1</td>
<td>5HSAA049630</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049630/1">UTR</a></td>
<td>URS0000DB2738_71657</td>
<td><a href="https://rnacentral.org/rna/URS0000DB2738/71657">RS</a></td>
<td>0.980</td>
<td>0.934</td>
<td>-51.719</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HMGB1">=></a></td>
</tr>
<tr>
<td>RSL24D1</td>
<td>5HSAA093429</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093429/1">UTR</a></td>
<td>URS00023305DA_1562698</td>
<td><a href="https://rnacentral.org/rna/URS00023305DA/1562698">RS</a></td>
<td>0.998</td>
<td>0.927</td>
<td>-51.111</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RSL24D1">=></a></td>
</tr>
<tr>
<td>ATL2</td>
<td>5HSAA008196</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA008196/1">UTR</a></td>
<td>URS0000E5FC2E_1660124</td>
<td><a href="https://rnacentral.org/rna/URS0000E5FC2E/1660124">RS</a></td>
<td>0.962</td>
<td>0.982</td>
<td>-8.225</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ATL2">=></a></td>
</tr>
<tr>
<td>TBCCD1</td>
<td>5HSAA107388</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA107388/1">UTR</a></td>
<td>URS0000C7408D_1321778</td>
<td><a href="https://rnacentral.org/rna/URS0000C7408D/1321778">RS</a></td>
<td>0.987</td>
<td>0.985</td>
<td>-4.026</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TBCCD1">=></a></td>
</tr>
<tr>
<td>GIMAP4</td>
<td>5HSAA044141</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA044141/1">UTR</a></td>
<td>URS0000AB9887_999541</td>
<td><a href="https://rnacentral.org/rna/URS0000AB9887/999541">RS</a></td>
<td>0.985</td>
<td>0.944</td>
<td>-35.544</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GIMAP4">=></a></td>
</tr>
<tr>
<td>PMF1</td>
<td>5HSAA081676</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA081676/1">UTR</a></td>
<td>URS0000E607AE_1797924</td>
<td><a href="https://rnacentral.org/rna/URS0000E607AE/1797924">RS</a></td>
<td>0.987</td>
<td>0.990</td>
<td>-11.178</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PMF1">=></a></td>
</tr>
<tr>
<td>MAD2L1BP</td>
<td>5HSAA061393</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA061393/1">UTR</a></td>
<td>URS0000D66F1A_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D66F1A/12908">RS</a></td>
<td>0.972</td>
<td>0.983</td>
<td>-22.376</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAD2L1BP">=></a></td>
</tr>
<tr>
<td>RBM8A</td>
<td>5HSAA089623</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089623/1">UTR</a></td>
<td>URS0000C409AC_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C409AC/12908">RS</a></td>
<td>0.974</td>
<td>0.982</td>
<td>-14.582</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RBM8A">=></a></td>
</tr>
<tr>
<td>NCAPH</td>
<td>5HSAA070478</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA070478/1">UTR</a></td>
<td>URS0000C6737E_1305675</td>
<td><a href="https://rnacentral.org/rna/URS0000C6737E/1305675">RS</a></td>
<td>0.967</td>
<td>0.951</td>
<td>-31.538</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NCAPH">=></a></td>
</tr>
<tr>
<td>SIRT6</td>
<td>5HSAA098484</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA098484/1">UTR</a></td>
<td>URS0000D696FF_1151274</td>
<td><a href="https://rnacentral.org/rna/URS0000D696FF/1151274">RS</a></td>
<td>0.943</td>
<td>0.974</td>
<td>-28.749</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SIRT6">=></a></td>
</tr>
<tr>
<td>PNPLA6</td>
<td>5HSAA081976</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA081976/1">UTR</a></td>
<td>URS0000C51AE8_1497020</td>
<td><a href="https://rnacentral.org/rna/URS0000C51AE8/1497020">RS</a></td>
<td>0.952</td>
<td>0.933</td>
<td>-31.521</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PNPLA6">=></a></td>
</tr>
<tr>
<td>TPRG1L</td>
<td>5HSAA113039</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA113039/1">UTR</a></td>
<td>URS0000D80070_1122209</td>
<td><a href="https://rnacentral.org/rna/URS0000D80070/1122209">RS</a></td>
<td>0.990</td>
<td>0.975</td>
<td>-27.481</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TPRG1L">=></a></td>
</tr>
<tr>
<td>THAP6</td>
<td>5HSAA108966</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA108966/1">UTR</a></td>
<td>URS0000C04ED6_1304275</td>
<td><a href="https://rnacentral.org/rna/URS0000C04ED6/1304275">RS</a></td>
<td>0.946</td>
<td>0.937</td>
<td>-48.260</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/THAP6">=></a></td>
</tr>
<tr>
<td>FKBP15</td>
<td>5HSAA041102</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA041102/1">UTR</a></td>
<td>URS0000C1DDE2_29363</td>
<td><a href="https://rnacentral.org/rna/URS0000C1DDE2/29363">RS</a></td>
<td>0.957</td>
<td>0.939</td>
<td>-55.182</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FKBP15">=></a></td>
</tr>
<tr>
<td>TMX2</td>
<td>5HSAA111794</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111794/1">UTR</a></td>
<td>URS0000ABAA6C_1302241</td>
<td><a href="https://rnacentral.org/rna/URS0000ABAA6C/1302241">RS</a></td>
<td>0.978</td>
<td>0.978</td>
<td>-24.482</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMX2">=></a></td>
</tr>
<tr>
<td>EEF2</td>
<td>5HSAA033473</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033473/1">UTR</a></td>
<td>URS0000C0F199_273678</td>
<td><a href="https://rnacentral.org/rna/URS0000C0F199/273678">RS</a></td>
<td>0.957</td>
<td>0.967</td>
<td>-34.267</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EEF2">=></a></td>
</tr>
<tr>
<td>EPB41L3</td>
<td>5HSAA035757</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035757/1">UTR</a></td>
<td>URS0000D6A741_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6A741/12908">RS</a></td>
<td>0.992</td>
<td>0.973</td>
<td>-12.909</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EPB41L3">=></a></td>
</tr>
<tr>
<td>IQUB</td>
<td>5HSAA053773</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA053773/1">UTR</a></td>
<td>URS0000AB515E_717774</td>
<td><a href="https://rnacentral.org/rna/URS0000AB515E/717774">RS</a></td>
<td>0.955</td>
<td>0.945</td>
<td>-28.813</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IQUB">=></a></td>
</tr>
<tr>
<td>FDPS</td>
<td>5HSAA040291</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA040291/1">UTR</a></td>
<td>URS0000DB6998_1895810</td>
<td><a href="https://rnacentral.org/rna/URS0000DB6998/1895810">RS</a></td>
<td>0.950</td>
<td>0.955</td>
<td>-46.978</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FDPS">=></a></td>
</tr>
<tr>
<td>GIN1</td>
<td>5HSAA044152</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA044152/1">UTR</a></td>
<td>URS0000C19243_1262784</td>
<td><a href="https://rnacentral.org/rna/URS0000C19243/1262784">RS</a></td>
<td>0.949</td>
<td>0.970</td>
<td>-23.498</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GIN1">=></a></td>
</tr>
<tr>
<td>COQ7</td>
<td>5HSAA024361-1</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024361-1/1">UTR</a></td>
<td>URS0000C850D4_1224163</td>
<td><a href="https://rnacentral.org/rna/URS0000C850D4/1224163">RS</a></td>
<td>0.954</td>
<td>0.967</td>
<td>-21.237</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COQ7">=></a></td>
</tr>
<tr>
<td>MED19</td>
<td>5HSAA064769</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064769/1">UTR</a></td>
<td>URS0000C257DF_505317</td>
<td><a href="https://rnacentral.org/rna/URS0000C257DF/505317">RS</a></td>
<td>0.991</td>
<td>0.985</td>
<td>-7.592</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED19">=></a></td>
</tr>
<tr>
<td>MPI</td>
<td>5HSAA067069-1</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067069-1/1">UTR</a></td>
<td>URS0000ABB2E4_272563</td>
<td><a href="https://rnacentral.org/rna/URS0000ABB2E4/272563">RS</a></td>
<td>0.959</td>
<td>0.976</td>
<td>-29.504</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MPI">=></a></td>
</tr>
<tr>
<td>ANAPC10</td>
<td>5HSAA004366</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004366/1">UTR</a></td>
<td>URS0000BA420C_1520</td>
<td><a href="https://rnacentral.org/rna/URS0000BA420C/1520">RS</a></td>
<td>0.952</td>
<td>0.932</td>
<td>-29.534</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ANAPC10">=></a></td>
</tr>
<tr>
<td>ZNF808</td>
<td>5HSAA123977</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123977/1">UTR</a></td>
<td>URS0000AB699B_665959</td>
<td><a href="https://rnacentral.org/rna/URS0000AB699B/665959">RS</a></td>
<td>0.999</td>
<td>0.952</td>
<td>-27.422</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF808">=></a></td>
</tr>
<tr>
<td>RSRC1</td>
<td>5HSAA093483</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093483/1">UTR</a></td>
<td>URS000231CFD4_159449</td>
<td><a href="https://rnacentral.org/rna/URS000231CFD4/159449">RS</a></td>
<td>0.999</td>
<td>0.952</td>
<td>-48.390</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RSRC1">=></a></td>
</tr>
<tr>
<td>CPNE5</td>
<td>5HSAA024789</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024789/1">UTR</a></td>
<td>URS000232A574_546414</td>
<td><a href="https://rnacentral.org/rna/URS000232A574/546414">RS</a></td>
<td>0.981</td>
<td>0.975</td>
<td>-20.081</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CPNE5">=></a></td>
</tr>
<tr>
<td>MED24</td>
<td>5HSAA064828</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064828/1">UTR</a></td>
<td>URS0000BFE945_1736303</td>
<td><a href="https://rnacentral.org/rna/URS0000BFE945/1736303">RS</a></td>
<td>0.975</td>
<td>0.965</td>
<td>-37.132</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED24">=></a></td>
</tr>
<tr>
<td>NXT2</td>
<td>5HSAA074674</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA074674/1">UTR</a></td>
<td>URS0000C1A032_1734395</td>
<td><a href="https://rnacentral.org/rna/URS0000C1A032/1734395">RS</a></td>
<td>0.983</td>
<td>0.963</td>
<td>-25.522</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NXT2">=></a></td>
</tr>
<tr>
<td>ANAPC10</td>
<td>5HSAA004375</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA004375/1">UTR</a></td>
<td>URS0000C29119_1121022</td>
<td><a href="https://rnacentral.org/rna/URS0000C29119/1121022">RS</a></td>
<td>0.971</td>
<td>0.960</td>
<td>-29.534</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ANAPC10">=></a></td>
</tr>
<tr>
<td>SNCAIP</td>
<td>5HSAA101881</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101881/1">UTR</a></td>
<td>URS0000C86F68_443610</td>
<td><a href="https://rnacentral.org/rna/URS0000C86F68/443610">RS</a></td>
<td>0.994</td>
<td>0.956</td>
<td>-32.204</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SNCAIP">=></a></td>
</tr>
<tr>
<td>CA7</td>
<td>5HSAA015961</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA015961/1">UTR</a></td>
<td>URS0000BE95E1_1732020</td>
<td><a href="https://rnacentral.org/rna/URS0000BE95E1/1732020">RS</a></td>
<td>0.992</td>
<td>0.954</td>
<td>-58.876</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CA7">=></a></td>
</tr>
<tr>
<td>HAGHL</td>
<td>5HSAA047795</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047795/1">UTR</a></td>
<td>URS0000D88F6F_114686</td>
<td><a href="https://rnacentral.org/rna/URS0000D88F6F/114686">RS</a></td>
<td>0.985</td>
<td>0.977</td>
<td>-28.525</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HAGHL">=></a></td>
</tr>
<tr>
<td>IFT81</td>
<td>5HSAA051937</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051937/1">UTR</a></td>
<td>URS0000D7EA3C_1897028</td>
<td><a href="https://rnacentral.org/rna/URS0000D7EA3C/1897028">RS</a></td>
<td>0.984</td>
<td>0.937</td>
<td>-42.719</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IFT81">=></a></td>
</tr>
<tr>
<td>ZNF292</td>
<td>5HSAA122589</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA122589/1">UTR</a></td>
<td>URS0000D9FB79_1805276</td>
<td><a href="https://rnacentral.org/rna/URS0000D9FB79/1805276">RS</a></td>
<td>0.965</td>
<td>0.979</td>
<td>-17.321</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF292">=></a></td>
</tr>
<tr>
<td>MCAT</td>
<td>5HSAA064156</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064156/1">UTR</a></td>
<td>URS00021EDEF5_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDEF5/12908">RS</a></td>
<td>0.995</td>
<td>0.985</td>
<td>-8.999</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MCAT">=></a></td>
</tr>
<tr>
<td>HSD17B7</td>
<td>5HSAA051003</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051003/1">UTR</a></td>
<td>URS0000C78DED_1206458</td>
<td><a href="https://rnacentral.org/rna/URS0000C78DED/1206458">RS</a></td>
<td>0.997</td>
<td>0.956</td>
<td>-39.584</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HSD17B7">=></a></td>
</tr>
<tr>
<td>PHF19</td>
<td>5HSAA079608</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA079608/1">UTR</a></td>
<td>URS0002325626_2020486</td>
<td><a href="https://rnacentral.org/rna/URS0002325626/2020486">RS</a></td>
<td>0.992</td>
<td>0.968</td>
<td>-27.899</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PHF19">=></a></td>
</tr>
<tr>
<td>ALDH18A1</td>
<td>5HSAA003585</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA003585/1">UTR</a></td>
<td>URS0000DAED65_310780</td>
<td><a href="https://rnacentral.org/rna/URS0000DAED65/310780">RS</a></td>
<td>0.968</td>
<td>0.953</td>
<td>-36.713</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ALDH18A1">=></a></td>
</tr>
<tr>
<td>MAPK15</td>
<td>5HSAA063291</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA063291/1">UTR</a></td>
<td>URS0002334230_34004</td>
<td><a href="https://rnacentral.org/rna/URS0002334230/34004">RS</a></td>
<td>0.970</td>
<td>0.978</td>
<td>-18.077</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAPK15">=></a></td>
</tr>
<tr>
<td>HHAT</td>
<td>5HSAA049101</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049101/1">UTR</a></td>
<td>URS00023120CD_1678840</td>
<td><a href="https://rnacentral.org/rna/URS00023120CD/1678840">RS</a></td>
<td>0.941</td>
<td>0.945</td>
<td>-43.489</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HHAT">=></a></td>
</tr>
<tr>
<td>DGUOK</td>
<td>5HSAA029879</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029879/1">UTR</a></td>
<td>URS0000C3A5C6_1548750</td>
<td><a href="https://rnacentral.org/rna/URS0000C3A5C6/1548750">RS</a></td>
<td>0.932</td>
<td>0.960</td>
<td>-37.928</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DGUOK">=></a></td>
</tr>
<tr>
<td>RBM46</td>
<td>5HSAA089522</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089522/1">UTR</a></td>
<td>URS0000AB84C4_380704</td>
<td><a href="https://rnacentral.org/rna/URS0000AB84C4/380704">RS</a></td>
<td>0.994</td>
<td>0.939</td>
<td>-54.597</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RBM46">=></a></td>
</tr>
<tr>
<td>CORO7</td>
<td>5HSAA024464</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024464/1">UTR</a></td>
<td>URS0000AB2B2B_386415</td>
<td><a href="https://rnacentral.org/rna/URS0000AB2B2B/386415">RS</a></td>
<td>0.998</td>
<td>0.968</td>
<td>-36.278</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CORO7">=></a></td>
</tr>
<tr>
<td>ADARB1</td>
<td>5HSAA002206</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA002206/1">UTR</a></td>
<td>URS0000C1ABB2_3708</td>
<td><a href="https://rnacentral.org/rna/URS0000C1ABB2/3708">RS</a></td>
<td>0.947</td>
<td>0.953</td>
<td>-21.125</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ADARB1">=></a></td>
</tr>
<tr>
<td>FKBP15</td>
<td>5HSAA041101</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA041101/1">UTR</a></td>
<td>URS0000D9C63A_1797663</td>
<td><a href="https://rnacentral.org/rna/URS0000D9C63A/1797663">RS</a></td>
<td>0.967</td>
<td>0.923</td>
<td>-55.182</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FKBP15">=></a></td>
</tr>
<tr>
<td>NUDT7</td>
<td>5HSAA074172</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA074172/1">UTR</a></td>
<td>URS0000C00C2F_1736420</td>
<td><a href="https://rnacentral.org/rna/URS0000C00C2F/1736420">RS</a></td>
<td>0.984</td>
<td>0.940</td>
<td>-20.444</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NUDT7">=></a></td>
</tr>
<tr>
<td>OMA1</td>
<td>5HSAA075094</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA075094/1">UTR</a></td>
<td>URS0000D9C0A5_1797346</td>
<td><a href="https://rnacentral.org/rna/URS0000D9C0A5/1797346">RS</a></td>
<td>0.975</td>
<td>0.950</td>
<td>-15.422</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/OMA1">=></a></td>
</tr>
<tr>
<td>PLXNC1</td>
<td>5HSAA081654</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA081654/1">UTR</a></td>
<td>URS0000D89A79_1895848</td>
<td><a href="https://rnacentral.org/rna/URS0000D89A79/1895848">RS</a></td>
<td>0.937</td>
<td>0.971</td>
<td>-36.100</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PLXNC1">=></a></td>
</tr>
<tr>
<td>SNCA</td>
<td>5HSAA101861</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101861/1">UTR</a></td>
<td>URS0000C4105E_1262940</td>
<td><a href="https://rnacentral.org/rna/URS0000C4105E/1262940">RS</a></td>
<td>0.973</td>
<td>0.967</td>
<td>-30.679</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SNCA">=></a></td>
</tr>
<tr>
<td>KRTCAP2</td>
<td>5HSAA057535</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057535/1">UTR</a></td>
<td>URS0000C5672B_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C5672B/12908">RS</a></td>
<td>0.998</td>
<td>0.988</td>
<td>-14.992</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KRTCAP2">=></a></td>
</tr>
<tr>
<td>FANCB</td>
<td>5HSAA039329</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039329/1">UTR</a></td>
<td>URS0002314756_768706</td>
<td><a href="https://rnacentral.org/rna/URS0002314756/768706">RS</a></td>
<td>0.947</td>
<td>0.950</td>
<td>-44.442</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FANCB">=></a></td>
</tr>
<tr>
<td>HOXC9</td>
<td>5HSAA050599</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050599/1">UTR</a></td>
<td>URS0000DA91D9_1121318</td>
<td><a href="https://rnacentral.org/rna/URS0000DA91D9/1121318">RS</a></td>
<td>0.992</td>
<td>0.964</td>
<td>-25.617</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXC9">=></a></td>
</tr>
<tr>
<td>NDUFB6</td>
<td>5HSAA071260</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071260/1">UTR</a></td>
<td>URS0002315471_1882757</td>
<td><a href="https://rnacentral.org/rna/URS0002315471/1882757">RS</a></td>
<td>0.995</td>
<td>0.928</td>
<td>-56.526</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NDUFB6">=></a></td>
</tr>
<tr>
<td>PUS7L</td>
<td>5HSAA086860</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086860/1">UTR</a></td>
<td>URS0000D945DF_1797196</td>
<td><a href="https://rnacentral.org/rna/URS0000D945DF/1797196">RS</a></td>
<td>0.978</td>
<td>0.926</td>
<td>-32.528</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PUS7L">=></a></td>
</tr>
<tr>
<td>TMEM117</td>
<td>5HSAA110421</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA110421/1">UTR</a></td>
<td>URS0000AB5917_764298</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5917/764298">RS</a></td>
<td>0.998</td>
<td>0.967</td>
<td>-22.223</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMEM117">=></a></td>
</tr>
<tr>
<td>TARDBP</td>
<td>5HSAA106934</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA106934/1">UTR</a></td>
<td>URS0000D90115_1802655</td>
<td><a href="https://rnacentral.org/rna/URS0000D90115/1802655">RS</a></td>
<td>1.000</td>
<td>0.954</td>
<td>-37.495</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TARDBP">=></a></td>
</tr>
<tr>
<td>HIPK3</td>
<td>5HSAA049231</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA049231/1">UTR</a></td>
<td>URS0000D8B43A_1419482</td>
<td><a href="https://rnacentral.org/rna/URS0000D8B43A/1419482">RS</a></td>
<td>0.956</td>
<td>0.968</td>
<td>-23.201</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HIPK3">=></a></td>
</tr>
<tr>
<td>CCDC73</td>
<td>5HSAA018631</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018631/1">UTR</a></td>
<td>URS0000DB5491_987057</td>
<td><a href="https://rnacentral.org/rna/URS0000DB5491/987057">RS</a></td>
<td>0.998</td>
<td>0.974</td>
<td>-7.173</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC73">=></a></td>
</tr>
<tr>
<td>CSN3</td>
<td>5HSAA025799</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA025799/1">UTR</a></td>
<td>URS0000C853B8_1268237</td>
<td><a href="https://rnacentral.org/rna/URS0000C853B8/1268237">RS</a></td>
<td>0.954</td>
<td>0.971</td>
<td>-16.866</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CSN3">=></a></td>
</tr>
<tr>
<td>EXOSC9</td>
<td>5HSAA037337</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA037337/1">UTR</a></td>
<td>URS0000AB6BE8_621372</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6BE8/621372">RS</a></td>
<td>0.966</td>
<td>0.959</td>
<td>-39.376</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EXOSC9">=></a></td>
</tr>
<tr>
<td>GOSR1</td>
<td>5HSAA045718</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA045718/1">UTR</a></td>
<td>URS0000D6BBBA_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6BBBA/12908">RS</a></td>
<td>0.985</td>
<td>0.983</td>
<td>-8.198</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GOSR1">=></a></td>
</tr>
<tr>
<td>PMF1</td>
<td>5HSAA081677</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA081677/1">UTR</a></td>
<td>URS0000E608E8_80878</td>
<td><a href="https://rnacentral.org/rna/URS0000E608E8/80878">RS</a></td>
<td>0.970</td>
<td>0.985</td>
<td>-11.178</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PMF1">=></a></td>
</tr>
<tr>
<td>GEM</td>
<td>5HSAA043806</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA043806/1">UTR</a></td>
<td>URS0000D9B0AD_1917422</td>
<td><a href="https://rnacentral.org/rna/URS0000D9B0AD/1917422">RS</a></td>
<td>0.985</td>
<td>0.928</td>
<td>-65.712</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GEM">=></a></td>
</tr>
<tr>
<td>JMJD8</td>
<td>5HSAA054527</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA054527/1">UTR</a></td>
<td>URS00021EDDB3_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDDB3/12908">RS</a></td>
<td>0.975</td>
<td>0.980</td>
<td>-38.477</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/JMJD8">=></a></td>
</tr>
<tr>
<td>ARL6IP5</td>
<td>5HSAA006680</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA006680/1">UTR</a></td>
<td>URS00021EDDE3_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDDE3/12908">RS</a></td>
<td>0.987</td>
<td>0.969</td>
<td>-22.378</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ARL6IP5">=></a></td>
</tr>
<tr>
<td>PSMA3</td>
<td>5HSAA085448</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085448/1">UTR</a></td>
<td>URS0000C6FB32_1736379</td>
<td><a href="https://rnacentral.org/rna/URS0000C6FB32/1736379">RS</a></td>
<td>0.945</td>
<td>0.977</td>
<td>-18.040</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMA3">=></a></td>
</tr>
<tr>
<td>ATF1</td>
<td>5HSAA007828</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA007828/1">UTR</a></td>
<td>URS0002321F93_1206781</td>
<td><a href="https://rnacentral.org/rna/URS0002321F93/1206781">RS</a></td>
<td>0.954</td>
<td>0.973</td>
<td>-14.488</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ATF1">=></a></td>
</tr>
<tr>
<td>CDK5</td>
<td>5HSAA020574</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA020574/1">UTR</a></td>
<td>URS0000D7E944_1299327</td>
<td><a href="https://rnacentral.org/rna/URS0000D7E944/1299327">RS</a></td>
<td>0.999</td>
<td>0.980</td>
<td>-20.594</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CDK5">=></a></td>
</tr>
<tr>
<td>FBXO25</td>
<td>5HSAA039823</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039823/1">UTR</a></td>
<td>URS0000BFF5A5_104623</td>
<td><a href="https://rnacentral.org/rna/URS0000BFF5A5/104623">RS</a></td>
<td>0.987</td>
<td>0.983</td>
<td>-12.508</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FBXO25">=></a></td>
</tr>
<tr>
<td>CCDC138</td>
<td>5HSAA018359</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018359/1">UTR</a></td>
<td>URS0000C20071_1587522</td>
<td><a href="https://rnacentral.org/rna/URS0000C20071/1587522">RS</a></td>
<td>0.996</td>
<td>0.981</td>
<td>-29.443</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC138">=></a></td>
</tr>
<tr>
<td>DNAJA1</td>
<td>5HSAA030808</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA030808/1">UTR</a></td>
<td>URS0000C06A4E_227882</td>
<td><a href="https://rnacentral.org/rna/URS0000C06A4E/227882">RS</a></td>
<td>0.956</td>
<td>0.967</td>
<td>-25.821</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DNAJA1">=></a></td>
</tr>
<tr>
<td>FCHSD2</td>
<td>5HSAA040128</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA040128/1">UTR</a></td>
<td>URS0002315D52_1302241</td>
<td><a href="https://rnacentral.org/rna/URS0002315D52/1302241">RS</a></td>
<td>0.984</td>
<td>0.919</td>
<td>-58.899</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FCHSD2">=></a></td>
</tr>
<tr>
<td>CCNK</td>
<td>5HSAA019014</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA019014/1">UTR</a></td>
<td>URS0002330821_1805632</td>
<td><a href="https://rnacentral.org/rna/URS0002330821/1805632">RS</a></td>
<td>0.968</td>
<td>0.941</td>
<td>-36.925</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCNK">=></a></td>
</tr>
<tr>
<td>FADS1</td>
<td>5HSAA037578-3</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA037578-3/1">UTR</a></td>
<td>URS0000AB2EBF_446469</td>
<td><a href="https://rnacentral.org/rna/URS0000AB2EBF/446469">RS</a></td>
<td>0.988</td>
<td>0.963</td>
<td>-44.948</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FADS1">=></a></td>
</tr>
<tr>
<td>AASDHPPT</td>
<td>5HSAA000187</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA000187/1">UTR</a></td>
<td>URS0000C7D5FA_1666916</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D5FA/1666916">RS</a></td>
<td>0.965</td>
<td>0.960</td>
<td>-21.419</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AASDHPPT">=></a></td>
</tr>
<tr>
<td>MED24</td>
<td>5HSAA064878</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064878/1">UTR</a></td>
<td>URS0000D78814_440512</td>
<td><a href="https://rnacentral.org/rna/URS0000D78814/440512">RS</a></td>
<td>0.996</td>
<td>0.945</td>
<td>-47.234</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED24">=></a></td>
</tr>
<tr>
<td>U2AF1L4</td>
<td>5HSAA115510</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115510/1">UTR</a></td>
<td>URS0000D6A371_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6A371/12908">RS</a></td>
<td>0.966</td>
<td>0.984</td>
<td>-15.270</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/U2AF1L4">=></a></td>
</tr>
<tr>
<td>ITPKC</td>
<td>5HSAA054303</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA054303/1">UTR</a></td>
<td>URS0000E60736_1523413</td>
<td><a href="https://rnacentral.org/rna/URS0000E60736/1523413">RS</a></td>
<td>0.991</td>
<td>0.971</td>
<td>-24.914</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ITPKC">=></a></td>
</tr>
<tr>
<td>ATRNL1</td>
<td>5HSAA008901</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA008901/1">UTR</a></td>
<td>URS0000C82C7E_1262977</td>
<td><a href="https://rnacentral.org/rna/URS0000C82C7E/1262977">RS</a></td>
<td>0.954</td>
<td>0.974</td>
<td>-22.029</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ATRNL1">=></a></td>
</tr>
<tr>
<td>DGKD</td>
<td>5HSAA029831</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029831/1">UTR</a></td>
<td>URS0000DB5154_1974213</td>
<td><a href="https://rnacentral.org/rna/URS0000DB5154/1974213">RS</a></td>
<td>0.956</td>
<td>0.960</td>
<td>-24.520</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DGKD">=></a></td>
</tr>
<tr>
<td>THAP9</td>
<td>5HSAA108986</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA108986/1">UTR</a></td>
<td>URS0000ABC78E_391624</td>
<td><a href="https://rnacentral.org/rna/URS0000ABC78E/391624">RS</a></td>
<td>0.996</td>
<td>0.950</td>
<td>-46.446</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/THAP9">=></a></td>
</tr>
<tr>
<td>METTL5</td>
<td>5HSAA065303</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA065303/1">UTR</a></td>
<td>URS0000AB5242_481743</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5242/481743">RS</a></td>
<td>0.987</td>
<td>0.956</td>
<td>-46.697</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/METTL5">=></a></td>
</tr>
<tr>
<td>PRMT1</td>
<td>5HSAA084852</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA084852/1">UTR</a></td>
<td>URS0000AB3BB1_298386</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3BB1/298386">RS</a></td>
<td>0.966</td>
<td>0.933</td>
<td>-56.139</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRMT1">=></a></td>
</tr>
<tr>
<td>ZBTB8OS</td>
<td>5HSAA121045</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA121045/1">UTR</a></td>
<td>URS00021EDE69_1356575</td>
<td><a href="https://rnacentral.org/rna/URS00021EDE69/1356575">RS</a></td>
<td>0.997</td>
<td>0.989</td>
<td>-11.660</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZBTB8OS">=></a></td>
</tr>
<tr>
<td>RSRC1</td>
<td>5HSAA093485</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093485/1">UTR</a></td>
<td>URS0000BEC048_2026</td>
<td><a href="https://rnacentral.org/rna/URS0000BEC048/2026">RS</a></td>
<td>0.974</td>
<td>0.950</td>
<td>-63.298</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RSRC1">=></a></td>
</tr>
<tr>
<td>PSMB3</td>
<td>5HSAA085509</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085509/1">UTR</a></td>
<td>URS0000DAFF57_1965603</td>
<td><a href="https://rnacentral.org/rna/URS0000DAFF57/1965603">RS</a></td>
<td>0.988</td>
<td>0.971</td>
<td>-20.663</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMB3">=></a></td>
</tr>
<tr>
<td>RUVBL2</td>
<td>5HSAA093770</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093770/1">UTR</a></td>
<td>URS00021EDC6D_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDC6D/12908">RS</a></td>
<td>0.962</td>
<td>0.977</td>
<td>-7.384</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RUVBL2">=></a></td>
</tr>
<tr>
<td>LBR</td>
<td>5HSAA058362</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA058362/1">UTR</a></td>
<td>URS0000D97FBD_1121291</td>
<td><a href="https://rnacentral.org/rna/URS0000D97FBD/1121291">RS</a></td>
<td>0.977</td>
<td>0.923</td>
<td>-35.886</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LBR">=></a></td>
</tr>
<tr>
<td>TXNDC8</td>
<td>5HSAA115355</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115355/1">UTR</a></td>
<td>URS0000AB5BD1_1655618</td>
<td><a href="https://rnacentral.org/rna/URS0000AB5BD1/1655618">RS</a></td>
<td>0.964</td>
<td>0.965</td>
<td>-12.866</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TXNDC8">=></a></td>
</tr>
<tr>
<td>TIGIT</td>
<td>5HSAA109440</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA109440/1">UTR</a></td>
<td>URS0000C36DF4_1345695</td>
<td><a href="https://rnacentral.org/rna/URS0000C36DF4/1345695">RS</a></td>
<td>0.972</td>
<td>0.976</td>
<td>-26.043</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TIGIT">=></a></td>
</tr>
<tr>
<td>MAPRE1</td>
<td>5HSAA063472</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA063472/1">UTR</a></td>
<td>URS0000D91BD8_1888891</td>
<td><a href="https://rnacentral.org/rna/URS0000D91BD8/1888891">RS</a></td>
<td>0.988</td>
<td>0.936</td>
<td>-55.496</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAPRE1">=></a></td>
</tr>
<tr>
<td>EPB41L3</td>
<td>5HSAA035737</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035737/1">UTR</a></td>
<td>URS0000C7804F_1236550</td>
<td><a href="https://rnacentral.org/rna/URS0000C7804F/1236550">RS</a></td>
<td>0.996</td>
<td>0.960</td>
<td>-36.003</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EPB41L3">=></a></td>
</tr>
<tr>
<td>TRPM6</td>
<td>5HSAA114063</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114063/1">UTR</a></td>
<td>URS0000D6C2FB_588581</td>
<td><a href="https://rnacentral.org/rna/URS0000D6C2FB/588581">RS</a></td>
<td>0.934</td>
<td>0.975</td>
<td>-16.220</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TRPM6">=></a></td>
</tr>
<tr>
<td>SATL1</td>
<td>5HSAA094554</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA094554/1">UTR</a></td>
<td>URS0000D97846_1797662</td>
<td><a href="https://rnacentral.org/rna/URS0000D97846/1797662">RS</a></td>
<td>0.994</td>
<td>0.983</td>
<td>-9.969</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SATL1">=></a></td>
</tr>
<tr>
<td>IGF2BP2</td>
<td>5HSAA052057</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA052057/1">UTR</a></td>
<td>URS0001ECA6E2_1308</td>
<td><a href="https://rnacentral.org/rna/URS0001ECA6E2/1308">RS</a></td>
<td>0.957</td>
<td>0.972</td>
<td>-17.724</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IGF2BP2">=></a></td>
</tr>
<tr>
<td>SAR1A</td>
<td>5HSAA094425</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA094425/1">UTR</a></td>
<td>URS0000D7BC72_1960125</td>
<td><a href="https://rnacentral.org/rna/URS0000D7BC72/1960125">RS</a></td>
<td>0.944</td>
<td>0.977</td>
<td>-24.235</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SAR1A">=></a></td>
</tr>
<tr>
<td>PTCH1</td>
<td>5HSAA085991</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085991/1">UTR</a></td>
<td>URS0000C35765_1263025</td>
<td><a href="https://rnacentral.org/rna/URS0000C35765/1263025">RS</a></td>
<td>0.944</td>
<td>0.938</td>
<td>-60.857</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PTCH1">=></a></td>
</tr>
<tr>
<td>RPS10</td>
<td>5HSAA092843</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092843/1">UTR</a></td>
<td>URS0000BECE8B_1321816</td>
<td><a href="https://rnacentral.org/rna/URS0000BECE8B/1321816">RS</a></td>
<td>0.985</td>
<td>0.969</td>
<td>-23.063</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS10">=></a></td>
</tr>
<tr>
<td>CCDC138</td>
<td>5HSAA018358</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018358/1">UTR</a></td>
<td>URS00021EDB8E_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDB8E/12908">RS</a></td>
<td>1.000</td>
<td>0.975</td>
<td>-37.243</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC138">=></a></td>
</tr>
<tr>
<td>TMEM50B</td>
<td>5HSAA111257</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111257/1">UTR</a></td>
<td>URS0000D945FA_163877</td>
<td><a href="https://rnacentral.org/rna/URS0000D945FA/163877">RS</a></td>
<td>0.979</td>
<td>0.959</td>
<td>-18.002</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMEM50B">=></a></td>
</tr>
<tr>
<td>TOM1</td>
<td>5HSAA112297-1</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA112297-1/1">UTR</a></td>
<td>URS0000C4B469_66876</td>
<td><a href="https://rnacentral.org/rna/URS0000C4B469/66876">RS</a></td>
<td>0.980</td>
<td>0.975</td>
<td>-34.520</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TOM1">=></a></td>
</tr>
<tr>
<td>COQ3</td>
<td>5HSAA024340</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024340/1">UTR</a></td>
<td>URS0000E5FAC1_1007105</td>
<td><a href="https://rnacentral.org/rna/URS0000E5FAC1/1007105">RS</a></td>
<td>0.940</td>
<td>0.976</td>
<td>-12.329</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COQ3">=></a></td>
</tr>
<tr>
<td>THADA</td>
<td>5HSAA108940</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA108940/1">UTR</a></td>
<td>URS0000BF91A3_692275</td>
<td><a href="https://rnacentral.org/rna/URS0000BF91A3/692275">RS</a></td>
<td>0.976</td>
<td>0.896</td>
<td>-48.782</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/THADA">=></a></td>
</tr>
<tr>
<td>WDR35</td>
<td>5HSAA119325</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA119325/1">UTR</a></td>
<td>URS0000C7D907_1090375</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D907/1090375">RS</a></td>
<td>0.951</td>
<td>0.956</td>
<td>-51.727</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/WDR35">=></a></td>
</tr>
<tr>
<td>MVD</td>
<td>5HSAA068889</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA068889/1">UTR</a></td>
<td>URS0000D674BA_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D674BA/12908">RS</a></td>
<td>0.996</td>
<td>0.971</td>
<td>-20.756</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MVD">=></a></td>
</tr>
<tr>
<td>MRPS17</td>
<td>5HSAA067622</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067622/1">UTR</a></td>
<td>URS0000BFC384_1574623</td>
<td><a href="https://rnacentral.org/rna/URS0000BFC384/1574623">RS</a></td>
<td>0.980</td>
<td>0.981</td>
<td>-14.188</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPS17">=></a></td>
</tr>
<tr>
<td>MRPL36</td>
<td>5HSAA067458</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067458/1">UTR</a></td>
<td>URS0000C839A3_1077972</td>
<td><a href="https://rnacentral.org/rna/URS0000C839A3/1077972">RS</a></td>
<td>0.976</td>
<td>0.967</td>
<td>-38.313</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPL36">=></a></td>
</tr>
<tr>
<td>DYNC1LI1</td>
<td>5HSAA032830</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA032830/1">UTR</a></td>
<td>URS0000D82DA3_47857</td>
<td><a href="https://rnacentral.org/rna/URS0000D82DA3/47857">RS</a></td>
<td>0.935</td>
<td>0.958</td>
<td>-55.924</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DYNC1LI1">=></a></td>
</tr>
<tr>
<td>RAD9B</td>
<td>5HSAA088286</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA088286/1">UTR</a></td>
<td>URS0000C21581_616990</td>
<td><a href="https://rnacentral.org/rna/URS0000C21581/616990">RS</a></td>
<td>0.960</td>
<td>0.933</td>
<td>-39.053</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RAD9B">=></a></td>
</tr>
<tr>
<td>MBD2</td>
<td>5HSAA064051</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064051/1">UTR</a></td>
<td>URS0000C01C65_1262708</td>
<td><a href="https://rnacentral.org/rna/URS0000C01C65/1262708">RS</a></td>
<td>0.999</td>
<td>0.904</td>
<td>-14.386</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MBD2">=></a></td>
</tr>
<tr>
<td>CCT6B</td>
<td>5HSAA019326</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA019326/1">UTR</a></td>
<td>URS0000AB3F62_1223307</td>
<td><a href="https://rnacentral.org/rna/URS0000AB3F62/1223307">RS</a></td>
<td>0.944</td>
<td>0.941</td>
<td>-29.901</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCT6B">=></a></td>
</tr>
<tr>
<td>RBM8A</td>
<td>5HSAA089624-1</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089624-1/1">UTR</a></td>
<td>URS0000DA8F5A_488446</td>
<td><a href="https://rnacentral.org/rna/URS0000DA8F5A/488446">RS</a></td>
<td>0.961</td>
<td>0.942</td>
<td>-44.876</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RBM8A">=></a></td>
</tr>
<tr>
<td>BBX</td>
<td>5HSAA010138</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010138/1">UTR</a></td>
<td>URS0000DA65BC_1797330</td>
<td><a href="https://rnacentral.org/rna/URS0000DA65BC/1797330">RS</a></td>
<td>0.971</td>
<td>0.980</td>
<td>-10.706</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BBX">=></a></td>
</tr>
<tr>
<td>DHCR7</td>
<td>5HSAA029904</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029904/1">UTR</a></td>
<td>URS0000AB46E8_66692</td>
<td><a href="https://rnacentral.org/rna/URS0000AB46E8/66692">RS</a></td>
<td>0.985</td>
<td>0.984</td>
<td>-5.316</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DHCR7">=></a></td>
</tr>
<tr>
<td>UTP18</td>
<td>5HSAA117907</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA117907/1">UTR</a></td>
<td>URS0000D86F2B_1797484</td>
<td><a href="https://rnacentral.org/rna/URS0000D86F2B/1797484">RS</a></td>
<td>0.998</td>
<td>0.972</td>
<td>-23.459</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UTP18">=></a></td>
</tr>
<tr>
<td>PEX11B</td>
<td>5HSAA078949</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA078949/1">UTR</a></td>
<td>URS0000C1B020_86416</td>
<td><a href="https://rnacentral.org/rna/URS0000C1B020/86416">RS</a></td>
<td>0.959</td>
<td>0.958</td>
<td>-38.267</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PEX11B">=></a></td>
</tr>
<tr>
<td>RAB3GAP1</td>
<td>5HSAA087523</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA087523/1">UTR</a></td>
<td>URS000010497E_204773</td>
<td><a href="https://rnacentral.org/rna/URS000010497E/204773">RS</a></td>
<td>0.955</td>
<td>0.945</td>
<td>-38.052</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RAB3GAP1">=></a></td>
</tr>
<tr>
<td>IDE</td>
<td>5HSAA051579</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051579/1">UTR</a></td>
<td>URS0000DAEDD0_683354</td>
<td><a href="https://rnacentral.org/rna/URS0000DAEDD0/683354">RS</a></td>
<td>0.982</td>
<td>0.976</td>
<td>-41.348</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IDE">=></a></td>
</tr>
<tr>
<td>MRPS10</td>
<td>5HSAA067583</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067583/1">UTR</a></td>
<td>URS00023300A3_1618477</td>
<td><a href="https://rnacentral.org/rna/URS00023300A3/1618477">RS</a></td>
<td>0.991</td>
<td>0.982</td>
<td>-29.151</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPS10">=></a></td>
</tr>
<tr>
<td>TNFRSF13B</td>
<td>5HSAA111883</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111883/1">UTR</a></td>
<td>URS0000E6020D_1134474</td>
<td><a href="https://rnacentral.org/rna/URS0000E6020D/1134474">RS</a></td>
<td>0.991</td>
<td>0.974</td>
<td>-12.838</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TNFRSF13B">=></a></td>
</tr>
<tr>
<td>HOXC9</td>
<td>5HSAA050600</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050600/1">UTR</a></td>
<td>URS0000AB1781_413999</td>
<td><a href="https://rnacentral.org/rna/URS0000AB1781/413999">RS</a></td>
<td>0.995</td>
<td>0.976</td>
<td>-21.218</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXC9">=></a></td>
</tr>
<tr>
<td>OTP</td>
<td>5HSAA075640</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA075640/1">UTR</a></td>
<td>URS0000C1823F_1262877</td>
<td><a href="https://rnacentral.org/rna/URS0000C1823F/1262877">RS</a></td>
<td>0.944</td>
<td>0.920</td>
<td>-36.703</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/OTP">=></a></td>
</tr>
<tr>
<td>PSMD9</td>
<td>5HSAA085707</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085707/1">UTR</a></td>
<td>URS0000AB487B_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000AB487B/12908">RS</a></td>
<td>0.933</td>
<td>0.973</td>
<td>-40.637</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMD9">=></a></td>
</tr>
<tr>
<td>EIF6</td>
<td>5HSAA034714</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA034714/1">UTR</a></td>
<td>URS0000BF1C63_1120923</td>
<td><a href="https://rnacentral.org/rna/URS0000BF1C63/1120923">RS</a></td>
<td>0.922</td>
<td>0.978</td>
<td>-28.557</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF6">=></a></td>
</tr>
<tr>
<td>MCAT</td>
<td>5HSAA064154</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064154/1">UTR</a></td>
<td>URS00021EDAB7_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDAB7/12908">RS</a></td>
<td>0.994</td>
<td>0.982</td>
<td>-29.600</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MCAT">=></a></td>
</tr>
<tr>
<td>AASDHPPT</td>
<td>5HSAA000186</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA000186/1">UTR</a></td>
<td>URS0000C7D5FA_1666916</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D5FA/1666916">RS</a></td>
<td>0.965</td>
<td>0.960</td>
<td>-21.419</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AASDHPPT">=></a></td>
</tr>
<tr>
<td>PRG4</td>
<td>5HSAA084384</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA084384/1">UTR</a></td>
<td>URS0000D681DF_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D681DF/12908">RS</a></td>
<td>0.990</td>
<td>0.978</td>
<td>-14.722</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRG4">=></a></td>
</tr>
<tr>
<td>EFTUD2</td>
<td>5HSAA033623</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033623/1">UTR</a></td>
<td>URS0000D6ABFA_1144317</td>
<td><a href="https://rnacentral.org/rna/URS0000D6ABFA/1144317">RS</a></td>
<td>0.975</td>
<td>0.977</td>
<td>-13.854</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EFTUD2">=></a></td>
</tr>
<tr>
<td>SLC35A2</td>
<td>5HSAA099856</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA099856/1">UTR</a></td>
<td>URS0000622302_272630</td>
<td><a href="https://rnacentral.org/rna/URS0000622302/272630">RS</a></td>
<td>0.964</td>
<td>0.942</td>
<td>-23.755</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SLC35A2">=></a></td>
</tr>
<tr>
<td>PUS10</td>
<td>5HSAA086844</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086844/1">UTR</a></td>
<td>URS0000BEF409_1262998</td>
<td><a href="https://rnacentral.org/rna/URS0000BEF409/1262998">RS</a></td>
<td>0.977</td>
<td>0.969</td>
<td>-27.130</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PUS10">=></a></td>
</tr>
<tr>
<td>EIF3I</td>
<td>5HSAA034280</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA034280/1">UTR</a></td>
<td>URS0000DA07F5_665914</td>
<td><a href="https://rnacentral.org/rna/URS0000DA07F5/665914">RS</a></td>
<td>0.983</td>
<td>0.967</td>
<td>-24.004</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF3I">=></a></td>
</tr>
<tr>
<td>SPDYA</td>
<td>5HSAA103232</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103232/1">UTR</a></td>
<td>URS00019BCB16_2653157</td>
<td><a href="https://rnacentral.org/rna/URS00019BCB16/2653157">RS</a></td>
<td>0.956</td>
<td>0.941</td>
<td>-58.254</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPDYA">=></a></td>
</tr>
<tr>
<td>THAP9</td>
<td>5HSAA108987</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA108987/1">UTR</a></td>
<td>URS0000D7C83F_307121</td>
<td><a href="https://rnacentral.org/rna/URS0000D7C83F/307121">RS</a></td>
<td>0.996</td>
<td>0.929</td>
<td>-42.216</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/THAP9">=></a></td>
</tr>
<tr>
<td>ZC3H7A</td>
<td>5HSAA121170</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA121170/1">UTR</a></td>
<td>URS0000C01AB6_929562</td>
<td><a href="https://rnacentral.org/rna/URS0000C01AB6/929562">RS</a></td>
<td>0.995</td>
<td>0.975</td>
<td>-8.867</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZC3H7A">=></a></td>
</tr>
<tr>
<td>TP63</td>
<td>5HSAA112679</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA112679/1">UTR</a></td>
<td>URS0000C3EAC9_408015</td>
<td><a href="https://rnacentral.org/rna/URS0000C3EAC9/408015">RS</a></td>
<td>0.969</td>
<td>0.949</td>
<td>-18.700</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TP63">=></a></td>
</tr>
<tr>
<td>MED24</td>
<td>5HSAA064831</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064831/1">UTR</a></td>
<td>URS0000C3697C_1218508</td>
<td><a href="https://rnacentral.org/rna/URS0000C3697C/1218508">RS</a></td>
<td>0.983</td>
<td>0.947</td>
<td>-43.169</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED24">=></a></td>
</tr>
<tr>
<td>LARP7</td>
<td>5HSAA057963</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057963/1">UTR</a></td>
<td>URS0000D8C782_1665556</td>
<td><a href="https://rnacentral.org/rna/URS0000D8C782/1665556">RS</a></td>
<td>0.956</td>
<td>0.970</td>
<td>-24.168</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LARP7">=></a></td>
</tr>
<tr>
<td>C1D</td>
<td>5HSAA013481</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA013481/1">UTR</a></td>
<td>URS0000BEDC68_321267</td>
<td><a href="https://rnacentral.org/rna/URS0000BEDC68/321267">RS</a></td>
<td>0.985</td>
<td>0.958</td>
<td>-18.086</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C1D">=></a></td>
</tr>
<tr>
<td>SLC25A3</td>
<td>5HSAA099252</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA099252/1">UTR</a></td>
<td>URS0000DAFD18_1122156</td>
<td><a href="https://rnacentral.org/rna/URS0000DAFD18/1122156">RS</a></td>
<td>0.976</td>
<td>0.955</td>
<td>-55.845</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SLC25A3">=></a></td>
</tr>
<tr>
<td>HOXA4</td>
<td>5HSAA050570</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050570/1">UTR</a></td>
<td>URS0000C2D4AA_1217659</td>
<td><a href="https://rnacentral.org/rna/URS0000C2D4AA/1217659">RS</a></td>
<td>0.990</td>
<td>0.985</td>
<td>-7.668</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXA4">=></a></td>
</tr>
<tr>
<td>TSPAN19</td>
<td>5HSAA114379</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114379/1">UTR</a></td>
<td>URS0000D7B2F1_1888891</td>
<td><a href="https://rnacentral.org/rna/URS0000D7B2F1/1888891">RS</a></td>
<td>0.986</td>
<td>0.954</td>
<td>-18.255</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TSPAN19">=></a></td>
</tr>
<tr>
<td>PPFIA1</td>
<td>5HSAA083103</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083103/1">UTR</a></td>
<td>URS0000C2C34D_1736524</td>
<td><a href="https://rnacentral.org/rna/URS0000C2C34D/1736524">RS</a></td>
<td>0.939</td>
<td>0.951</td>
<td>-49.407</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPFIA1">=></a></td>
</tr>
<tr>
<td>UQCRH</td>
<td>5HSAA117210</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA117210/1">UTR</a></td>
<td>URS00021EDF9C_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDF9C/12908">RS</a></td>
<td>0.948</td>
<td>0.976</td>
<td>-25.255</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UQCRH">=></a></td>
</tr>
<tr>
<td>COPB2</td>
<td>5HSAA024186</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024186/1">UTR</a></td>
<td>URS0000DAACF2_249567</td>
<td><a href="https://rnacentral.org/rna/URS0000DAACF2/249567">RS</a></td>
<td>0.997</td>
<td>0.878</td>
<td>-43.068</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COPB2">=></a></td>
</tr>
<tr>
<td>TRAPPC2L</td>
<td>5HSAA113314</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA113314/1">UTR</a></td>
<td>URS0000D8EEE3_1739315</td>
<td><a href="https://rnacentral.org/rna/URS0000D8EEE3/1739315">RS</a></td>
<td>0.974</td>
<td>0.977</td>
<td>-30.925</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TRAPPC2L">=></a></td>
</tr>
<tr>
<td>NDUFS1</td>
<td>5HSAA071293</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071293/1">UTR</a></td>
<td>URS0000C58DA8_121719</td>
<td><a href="https://rnacentral.org/rna/URS0000C58DA8/121719">RS</a></td>
<td>0.953</td>
<td>0.938</td>
<td>-42.039</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NDUFS1">=></a></td>
</tr>
<tr>
<td>POLR2B</td>
<td>5HSAA082391</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA082391/1">UTR</a></td>
<td>URS0000D8D378_1834193</td>
<td><a href="https://rnacentral.org/rna/URS0000D8D378/1834193">RS</a></td>
<td>0.994</td>
<td>0.980</td>
<td>-16.098</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/POLR2B">=></a></td>
</tr>
<tr>
<td>VPS33A</td>
<td>5HSAA118403</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA118403/1">UTR</a></td>
<td>URS0002321412_1817753</td>
<td><a href="https://rnacentral.org/rna/URS0002321412/1817753">RS</a></td>
<td>0.985</td>
<td>0.950</td>
<td>-66.275</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/VPS33A">=></a></td>
</tr>
<tr>
<td>PNPO</td>
<td>5HSAA082032</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA082032/1">UTR</a></td>
<td>URS0000C3D6B4_1111454</td>
<td><a href="https://rnacentral.org/rna/URS0000C3D6B4/1111454">RS</a></td>
<td>0.980</td>
<td>0.973</td>
<td>-35.372</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PNPO">=></a></td>
</tr>
<tr>
<td>SMC4</td>
<td>5HSAA101353</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101353/1">UTR</a></td>
<td>URS0000AB1D31_518637</td>
<td><a href="https://rnacentral.org/rna/URS0000AB1D31/518637">RS</a></td>
<td>0.990</td>
<td>0.971</td>
<td>-24.416</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SMC4">=></a></td>
</tr>
<tr>
<td>IFITM2</td>
<td>5HSAA051795</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051795/1">UTR</a></td>
<td>URS0000C5CFFD_1150591</td>
<td><a href="https://rnacentral.org/rna/URS0000C5CFFD/1150591">RS</a></td>
<td>0.982</td>
<td>0.939</td>
<td>-24.408</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IFITM2">=></a></td>
</tr>
<tr>
<td>VRK1</td>
<td>5HSAA118620</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA118620/1">UTR</a></td>
<td>URS0000C52E01_58291</td>
<td><a href="https://rnacentral.org/rna/URS0000C52E01/58291">RS</a></td>
<td>0.996</td>
<td>0.930</td>
<td>-49.818</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/VRK1">=></a></td>
</tr>
<tr>
<td>RNMT</td>
<td>5HSAA091923</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA091923/1">UTR</a></td>
<td>URS0000C305D4_1532558</td>
<td><a href="https://rnacentral.org/rna/URS0000C305D4/1532558">RS</a></td>
<td>0.962</td>
<td>0.925</td>
<td>-35.479</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RNMT">=></a></td>
</tr>
<tr>
<td>RXFP2</td>
<td>5HSAA093834</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093834/1">UTR</a></td>
<td>URS0000AB82D1_1834515</td>
<td><a href="https://rnacentral.org/rna/URS0000AB82D1/1834515">RS</a></td>
<td>0.984</td>
<td>0.974</td>
<td>-11.260</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RXFP2">=></a></td>
</tr>
<tr>
<td>PEX1</td>
<td>5HSAA078930</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA078930/1">UTR</a></td>
<td>URS0000C0E412_1712029</td>
<td><a href="https://rnacentral.org/rna/URS0000C0E412/1712029">RS</a></td>
<td>0.963</td>
<td>0.966</td>
<td>-55.748</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PEX1">=></a></td>
</tr>
<tr>
<td>SIRT5</td>
<td>5HSAA098449</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA098449/1">UTR</a></td>
<td>URS0000C2CDF2_1081108</td>
<td><a href="https://rnacentral.org/rna/URS0000C2CDF2/1081108">RS</a></td>
<td>0.978</td>
<td>0.935</td>
<td>-28.759</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SIRT5">=></a></td>
</tr>
<tr>
<td>SEC24C</td>
<td>5HSAA095783</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095783/1">UTR</a></td>
<td>URS0000AB985D_446465</td>
<td><a href="https://rnacentral.org/rna/URS0000AB985D/446465">RS</a></td>
<td>0.997</td>
<td>0.963</td>
<td>-32.285</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SEC24C">=></a></td>
</tr>
<tr>
<td>NCAPH</td>
<td>5HSAA070477</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA070477/1">UTR</a></td>
<td>URS0000AB53FC_399726</td>
<td><a href="https://rnacentral.org/rna/URS0000AB53FC/399726">RS</a></td>
<td>0.961</td>
<td>0.969</td>
<td>-29.442</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NCAPH">=></a></td>
</tr>
<tr>
<td>EIF1</td>
<td>5HSAA033819</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033819/1">UTR</a></td>
<td>URS0000C3FB39_1149862</td>
<td><a href="https://rnacentral.org/rna/URS0000C3FB39/1149862">RS</a></td>
<td>0.982</td>
<td>0.971</td>
<td>-6.394</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF1">=></a></td>
</tr>
<tr>
<td>LRRC43</td>
<td>5HSAA060547</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA060547/1">UTR</a></td>
<td>URS0000D68771_767455</td>
<td><a href="https://rnacentral.org/rna/URS0000D68771/767455">RS</a></td>
<td>0.979</td>
<td>0.988</td>
<td>-19.171</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LRRC43">=></a></td>
</tr>
<tr>
<td>CASZ1</td>
<td>5HSAA017865</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA017865/1">UTR</a></td>
<td>URS00023180C2_1458307</td>
<td><a href="https://rnacentral.org/rna/URS00023180C2/1458307">RS</a></td>
<td>0.959</td>
<td>0.934</td>
<td>-53.135</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CASZ1">=></a></td>
</tr>
<tr>
<td>MED24</td>
<td>5HSAA064867</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064867/1">UTR</a></td>
<td>URS0000D9B850_1798509</td>
<td><a href="https://rnacentral.org/rna/URS0000D9B850/1798509">RS</a></td>
<td>0.992</td>
<td>0.965</td>
<td>-23.183</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED24">=></a></td>
</tr>
<tr>
<td>MRPS17</td>
<td>5HSAA067619</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067619/1">UTR</a></td>
<td>URS00021EDBFC_1889778</td>
<td><a href="https://rnacentral.org/rna/URS00021EDBFC/1889778">RS</a></td>
<td>0.981</td>
<td>0.984</td>
<td>-4.080</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPS17">=></a></td>
</tr>
<tr>
<td>GNL2</td>
<td>5HSAA045360</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA045360/1">UTR</a></td>
<td>URS0002312B19_469618</td>
<td><a href="https://rnacentral.org/rna/URS0002312B19/469618">RS</a></td>
<td>0.987</td>
<td>0.920</td>
<td>-63.900</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GNL2">=></a></td>
</tr>
<tr>
<td>FANCM</td>
<td>5HSAA039400</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039400/1">UTR</a></td>
<td>URS0000AB8DAC_2604047</td>
<td><a href="https://rnacentral.org/rna/URS0000AB8DAC/2604047">RS</a></td>
<td>0.995</td>
<td>0.966</td>
<td>-41.136</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FANCM">=></a></td>
</tr>
<tr>
<td>MED24</td>
<td>5HSAA064824</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064824/1">UTR</a></td>
<td>URS0000AB4AB1_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000AB4AB1/12908">RS</a></td>
<td>1.000</td>
<td>0.958</td>
<td>-38.622</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED24">=></a></td>
</tr>
<tr>
<td>WWC3</td>
<td>5HSAA119999</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA119999/1">UTR</a></td>
<td>URS000231E58E_267128</td>
<td><a href="https://rnacentral.org/rna/URS000231E58E/267128">RS</a></td>
<td>0.990</td>
<td>0.920</td>
<td>-62.806</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/WWC3">=></a></td>
</tr>
<tr>
<td>BMI1</td>
<td>5HSAA010720</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010720/1">UTR</a></td>
<td>URS000231E957_716816</td>
<td><a href="https://rnacentral.org/rna/URS000231E957/716816">RS</a></td>
<td>0.988</td>
<td>0.962</td>
<td>-45.414</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BMI1">=></a></td>
</tr>
<tr>
<td>ZNF480</td>
<td>5HSAA123102</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123102/1">UTR</a></td>
<td>URS0000C57B6D_1538639</td>
<td><a href="https://rnacentral.org/rna/URS0000C57B6D/1538639">RS</a></td>
<td>0.951</td>
<td>0.971</td>
<td>-26.273</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF480">=></a></td>
</tr>
<tr>
<td>TSPAN5</td>
<td>5HSAA114421</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114421/1">UTR</a></td>
<td>URS0000C3969F_1423731</td>
<td><a href="https://rnacentral.org/rna/URS0000C3969F/1423731">RS</a></td>
<td>0.973</td>
<td>0.976</td>
<td>-11.862</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TSPAN5">=></a></td>
</tr>
<tr>
<td>PPIA</td>
<td>5HSAA083309-0</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083309-0/1">UTR</a></td>
<td>URS0000C4BE96_77044</td>
<td><a href="https://rnacentral.org/rna/URS0000C4BE96/77044">RS</a></td>
<td>0.984</td>
<td>0.946</td>
<td>-63.792</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPIA">=></a></td>
</tr>
<tr>
<td>EIF3C</td>
<td>5HSAA034128</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA034128/1">UTR</a></td>
<td>URS0000D842F9_214095</td>
<td><a href="https://rnacentral.org/rna/URS0000D842F9/214095">RS</a></td>
<td>0.925</td>
<td>0.965</td>
<td>-32.694</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EIF3C">=></a></td>
</tr>
<tr>
<td>PIGA</td>
<td>5HSAA080156</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080156/1">UTR</a></td>
<td>URS000232EB72_1736379</td>
<td><a href="https://rnacentral.org/rna/URS000232EB72/1736379">RS</a></td>
<td>0.987</td>
<td>0.948</td>
<td>-38.462</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PIGA">=></a></td>
</tr>
<tr>
<td>SERF2</td>
<td>5HSAA096469</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA096469/1">UTR</a></td>
<td>URS0000C2EE4D_1703405</td>
<td><a href="https://rnacentral.org/rna/URS0000C2EE4D/1703405">RS</a></td>
<td>1.000</td>
<td>0.941</td>
<td>-40.358</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SERF2">=></a></td>
</tr>
<tr>
<td>TMEM139</td>
<td>5HSAA110552</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA110552/1">UTR</a></td>
<td>URS0000C5CF1B_1185766</td>
<td><a href="https://rnacentral.org/rna/URS0000C5CF1B/1185766">RS</a></td>
<td>0.986</td>
<td>0.954</td>
<td>-32.139</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMEM139">=></a></td>
</tr>
<tr>
<td>NDUFA8</td>
<td>5HSAA071188</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA071188/1">UTR</a></td>
<td>URS0000D6B61F_333990</td>
<td><a href="https://rnacentral.org/rna/URS0000D6B61F/333990">RS</a></td>
<td>0.988</td>
<td>0.989</td>
<td>-8.986</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NDUFA8">=></a></td>
</tr>
<tr>
<td>TRMT5</td>
<td>5HSAA113890</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA113890/1">UTR</a></td>
<td>URS0000C39244_1736420</td>
<td><a href="https://rnacentral.org/rna/URS0000C39244/1736420">RS</a></td>
<td>0.940</td>
<td>0.962</td>
<td>-36.722</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TRMT5">=></a></td>
</tr>
<tr>
<td>MED29</td>
<td>5HSAA064915</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064915/1">UTR</a></td>
<td>URS0000D7F501_1581067</td>
<td><a href="https://rnacentral.org/rna/URS0000D7F501/1581067">RS</a></td>
<td>0.969</td>
<td>0.978</td>
<td>-7.427</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MED29">=></a></td>
</tr>
<tr>
<td>RS1</td>
<td>5HSAA093391</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA093391/1">UTR</a></td>
<td>URS0000BE357E_405566</td>
<td><a href="https://rnacentral.org/rna/URS0000BE357E/405566">RS</a></td>
<td>0.965</td>
<td>0.981</td>
<td>-6.284</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RS1">=></a></td>
</tr>
<tr>
<td>FAM8A1</td>
<td>5HSAA039154</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039154/1">UTR</a></td>
<td>URS0000BEF56C_1417296</td>
<td><a href="https://rnacentral.org/rna/URS0000BEF56C/1417296">RS</a></td>
<td>0.982</td>
<td>0.970</td>
<td>-23.191</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FAM8A1">=></a></td>
</tr>
<tr>
<td>CCNE2</td>
<td>5HSAA018950</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018950/1">UTR</a></td>
<td>URS0000C321FE_943816</td>
<td><a href="https://rnacentral.org/rna/URS0000C321FE/943816">RS</a></td>
<td>0.969</td>
<td>0.955</td>
<td>-53.248</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCNE2">=></a></td>
</tr>
<tr>
<td>LGSN</td>
<td>5HSAA058832</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA058832/1">UTR</a></td>
<td>URS0000E60321_1736382</td>
<td><a href="https://rnacentral.org/rna/URS0000E60321/1736382">RS</a></td>
<td>0.970</td>
<td>0.985</td>
<td>-12.710</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LGSN">=></a></td>
</tr>
<tr>
<td>APEX1</td>
<td>5HSAA005610</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA005610/1">UTR</a></td>
<td>URS0000AB24C6_323097</td>
<td><a href="https://rnacentral.org/rna/URS0000AB24C6/323097">RS</a></td>
<td>0.991</td>
<td>0.958</td>
<td>-45.022</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/APEX1">=></a></td>
</tr>
<tr>
<td>FASTKD3</td>
<td>5HSAA039555</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039555/1">UTR</a></td>
<td>URS0000D7D8E2_1965583</td>
<td><a href="https://rnacentral.org/rna/URS0000D7D8E2/1965583">RS</a></td>
<td>0.919</td>
<td>0.938</td>
<td>-33.067</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FASTKD3">=></a></td>
</tr>
<tr>
<td>NOP10</td>
<td>5HSAA072790</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA072790/1">UTR</a></td>
<td>URS0000C75D95_1150864</td>
<td><a href="https://rnacentral.org/rna/URS0000C75D95/1150864">RS</a></td>
<td>0.995</td>
<td>0.956</td>
<td>-33.879</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NOP10">=></a></td>
</tr>
<tr>
<td>EPHA7</td>
<td>5HSAA036089</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA036089/1">UTR</a></td>
<td>URS0002326C1D_60547</td>
<td><a href="https://rnacentral.org/rna/URS0002326C1D/60547">RS</a></td>
<td>0.961</td>
<td>0.895</td>
<td>-57.927</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EPHA7">=></a></td>
</tr>
<tr>
<td>GALNT1</td>
<td>5HSAA042859</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA042859/1">UTR</a></td>
<td>URS0000C505C6_936756</td>
<td><a href="https://rnacentral.org/rna/URS0000C505C6/936756">RS</a></td>
<td>0.940</td>
<td>0.962</td>
<td>-19.429</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GALNT1">=></a></td>
</tr>
<tr>
<td>TTPAL</td>
<td>5HSAA114958</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114958/1">UTR</a></td>
<td>URS0000C11709_1184607</td>
<td><a href="https://rnacentral.org/rna/URS0000C11709/1184607">RS</a></td>
<td>0.972</td>
<td>0.919</td>
<td>-65.273</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TTPAL">=></a></td>
</tr>
<tr>
<td>COG1</td>
<td>5HSAA023591</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA023591/1">UTR</a></td>
<td>URS0000DA1D41_1801684</td>
<td><a href="https://rnacentral.org/rna/URS0000DA1D41/1801684">RS</a></td>
<td>0.992</td>
<td>0.983</td>
<td>-20.388</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COG1">=></a></td>
</tr>
<tr>
<td>KCNK3</td>
<td>5HSAA054925</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA054925/1">UTR</a></td>
<td>URS0000DA51E5_1536774</td>
<td><a href="https://rnacentral.org/rna/URS0000DA51E5/1536774">RS</a></td>
<td>0.995</td>
<td>0.940</td>
<td>-37.388</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KCNK3">=></a></td>
</tr>
<tr>
<td>CHURC1</td>
<td>5HSAA022073</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA022073/1">UTR</a></td>
<td>URS0000D8BB1B_1665556</td>
<td><a href="https://rnacentral.org/rna/URS0000D8BB1B/1665556">RS</a></td>
<td>0.975</td>
<td>0.915</td>
<td>-55.962</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CHURC1">=></a></td>
</tr>
<tr>
<td>LLPH</td>
<td>5HSAA059279</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059279/1">UTR</a></td>
<td>URS0000C85852_1423755</td>
<td><a href="https://rnacentral.org/rna/URS0000C85852/1423755">RS</a></td>
<td>0.952</td>
<td>0.961</td>
<td>-42.894</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LLPH">=></a></td>
</tr>
<tr>
<td>ARID2</td>
<td>5HSAA006556</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA006556/1">UTR</a></td>
<td>URS0000C7D0E7_1196094</td>
<td><a href="https://rnacentral.org/rna/URS0000C7D0E7/1196094">RS</a></td>
<td>0.978</td>
<td>0.986</td>
<td>-6.196</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ARID2">=></a></td>
</tr>
<tr>
<td>HSPE1</td>
<td>5HSAA051260</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051260/1">UTR</a></td>
<td>URS000232B499_1246626</td>
<td><a href="https://rnacentral.org/rna/URS000232B499/1246626">RS</a></td>
<td>0.966</td>
<td>0.954</td>
<td>-23.511</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HSPE1">=></a></td>
</tr>
<tr>
<td>MAPRE1</td>
<td>5HSAA063487</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA063487/1">UTR</a></td>
<td>URS0000BFE73E_36809</td>
<td><a href="https://rnacentral.org/rna/URS0000BFE73E/36809">RS</a></td>
<td>0.951</td>
<td>0.980</td>
<td>-23.760</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MAPRE1">=></a></td>
</tr>
<tr>
<td>NBN</td>
<td>5HSAA070334</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA070334/1">UTR</a></td>
<td>URS0000ABD283_176279</td>
<td><a href="https://rnacentral.org/rna/URS0000ABD283/176279">RS</a></td>
<td>0.980</td>
<td>0.950</td>
<td>-50.645</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NBN">=></a></td>
</tr>
<tr>
<td>DFFA</td>
<td>5HSAA029710</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029710/1">UTR</a></td>
<td>URS0000AB34CC_159087</td>
<td><a href="https://rnacentral.org/rna/URS0000AB34CC/159087">RS</a></td>
<td>0.962</td>
<td>0.960</td>
<td>-59.252</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DFFA">=></a></td>
</tr>
<tr>
<td>RPL21</td>
<td>5HSAA092451</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092451/1">UTR</a></td>
<td>URS0000D99FD4_225004</td>
<td><a href="https://rnacentral.org/rna/URS0000D99FD4/225004">RS</a></td>
<td>0.930</td>
<td>0.951</td>
<td>-28.300</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL21">=></a></td>
</tr>
<tr>
<td>EEF2</td>
<td>5HSAA033474</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033474/1">UTR</a></td>
<td>URS0000C745B6_1797883</td>
<td><a href="https://rnacentral.org/rna/URS0000C745B6/1797883">RS</a></td>
<td>0.949</td>
<td>0.973</td>
<td>-34.267</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EEF2">=></a></td>
</tr>
<tr>
<td>PRSS27</td>
<td>5HSAA085279</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085279/1">UTR</a></td>
<td>URS0000AB1A13_257314</td>
<td><a href="https://rnacentral.org/rna/URS0000AB1A13/257314">RS</a></td>
<td>1.000</td>
<td>0.974</td>
<td>-14.802</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRSS27">=></a></td>
</tr>
<tr>
<td>SS18L2</td>
<td>5HSAA103988</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103988/1">UTR</a></td>
<td>URS0000C621DD_913325</td>
<td><a href="https://rnacentral.org/rna/URS0000C621DD/913325">RS</a></td>
<td>0.986</td>
<td>0.962</td>
<td>-41.354</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SS18L2">=></a></td>
</tr>
<tr>
<td>HAO1</td>
<td>5HSAA047816</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047816/1">UTR</a></td>
<td>URS0000264041_483908</td>
<td><a href="https://rnacentral.org/rna/URS0000264041/483908">RS</a></td>
<td>0.986</td>
<td>0.991</td>
<td>-9.709</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HAO1">=></a></td>
</tr>
<tr>
<td>NUDT7</td>
<td>5HSAA074167</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA074167/1">UTR</a></td>
<td>URS00008116B0_32630</td>
<td><a href="https://rnacentral.org/rna/URS00008116B0/32630">RS</a></td>
<td>0.965</td>
<td>0.971</td>
<td>-26.053</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/NUDT7">=></a></td>
</tr>
<tr>
<td>HOXA5</td>
<td>5HSAA050571</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050571/1">UTR</a></td>
<td>URS0000C626D0_1849168</td>
<td><a href="https://rnacentral.org/rna/URS0000C626D0/1849168">RS</a></td>
<td>0.992</td>
<td>0.973</td>
<td>-9.884</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXA5">=></a></td>
</tr>
<tr>
<td>ZNF480</td>
<td>5HSAA123103</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123103/1">UTR</a></td>
<td>URS0000ABB6D4_1002809</td>
<td><a href="https://rnacentral.org/rna/URS0000ABB6D4/1002809">RS</a></td>
<td>0.956</td>
<td>0.978</td>
<td>-28.578</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF480">=></a></td>
</tr>
<tr>
<td>PTPN3</td>
<td>5HSAA086439</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086439/1">UTR</a></td>
<td>URS0000DA20FB_1279029</td>
<td><a href="https://rnacentral.org/rna/URS0000DA20FB/1279029">RS</a></td>
<td>0.971</td>
<td>0.952</td>
<td>-59.669</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PTPN3">=></a></td>
</tr>
<tr>
<td>MOSPD2</td>
<td>5HSAA066968</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA066968/1">UTR</a></td>
<td>URS0000C00567_1380770</td>
<td><a href="https://rnacentral.org/rna/URS0000C00567/1380770">RS</a></td>
<td>1.000</td>
<td>0.919</td>
<td>-35.038</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MOSPD2">=></a></td>
</tr>
<tr>
<td>ENY2</td>
<td>5HSAA035640</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035640/1">UTR</a></td>
<td>URS0000C51FD1_1286171</td>
<td><a href="https://rnacentral.org/rna/URS0000C51FD1/1286171">RS</a></td>
<td>0.944</td>
<td>0.975</td>
<td>-23.298</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ENY2">=></a></td>
</tr>
<tr>
<td>COQ9</td>
<td>5HSAA024370</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA024370/1">UTR</a></td>
<td>URS0000C4DF16_86668</td>
<td><a href="https://rnacentral.org/rna/URS0000C4DF16/86668">RS</a></td>
<td>0.978</td>
<td>0.959</td>
<td>-48.558</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/COQ9">=></a></td>
</tr>
<tr>
<td>PLCB4</td>
<td>5HSAA080981</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080981/1">UTR</a></td>
<td>URS0000C754D5_229535</td>
<td><a href="https://rnacentral.org/rna/URS0000C754D5/229535">RS</a></td>
<td>0.973</td>
<td>0.966</td>
<td>-37.295</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PLCB4">=></a></td>
</tr>
<tr>
<td>FOXB1</td>
<td>5HSAA041681</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA041681/1">UTR</a></td>
<td>URS00021EDD4A_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDD4A/12908">RS</a></td>
<td>0.987</td>
<td>0.979</td>
<td>-9.489</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FOXB1">=></a></td>
</tr>
<tr>
<td>IFT88</td>
<td>5HSAA052015</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA052015/1">UTR</a></td>
<td>URS0000D7B577_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000D7B577/3562">RS</a></td>
<td>0.977</td>
<td>0.957</td>
<td>-26.841</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/IFT88">=></a></td>
</tr>
<tr>
<td>PRDX3</td>
<td>5HSAA084288</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA084288/1">UTR</a></td>
<td>URS0000AB6FCA_200446</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6FCA/200446">RS</a></td>
<td>0.951</td>
<td>0.939</td>
<td>-33.473</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRDX3">=></a></td>
</tr>
<tr>
<td>PTPN3</td>
<td>5HSAA086435</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA086435/1">UTR</a></td>
<td>URS00021EDC63_1300350</td>
<td><a href="https://rnacentral.org/rna/URS00021EDC63/1300350">RS</a></td>
<td>0.992</td>
<td>0.993</td>
<td>-4.259</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PTPN3">=></a></td>
</tr>
<tr>
<td>CDK5</td>
<td>5HSAA020573</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA020573/1">UTR</a></td>
<td>URS0000C81C99_1263022</td>
<td><a href="https://rnacentral.org/rna/URS0000C81C99/1263022">RS</a></td>
<td>0.995</td>
<td>0.972</td>
<td>-30.799</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CDK5">=></a></td>
</tr>
<tr>
<td>GTPBP6</td>
<td>5HSAA047442</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA047442/1">UTR</a></td>
<td>URS0000D6BBE7_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6BBE7/12908">RS</a></td>
<td>0.985</td>
<td>0.977</td>
<td>-29.083</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GTPBP6">=></a></td>
</tr>
<tr>
<td>PHF5A</td>
<td>5HSAA079759</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA079759/1">UTR</a></td>
<td>URS0000BE30EE_1736464</td>
<td><a href="https://rnacentral.org/rna/URS0000BE30EE/1736464">RS</a></td>
<td>0.972</td>
<td>0.974</td>
<td>-26.294</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PHF5A">=></a></td>
</tr>
<tr>
<td>ZNF688</td>
<td>5HSAA123714</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123714/1">UTR</a></td>
<td>URS0000C36402_1566358</td>
<td><a href="https://rnacentral.org/rna/URS0000C36402/1566358">RS</a></td>
<td>0.942</td>
<td>0.943</td>
<td>-55.459</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF688">=></a></td>
</tr>
<tr>
<td>PAM</td>
<td>5HSAA076470</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA076470/1">UTR</a></td>
<td>URS0000C08F20_1080227</td>
<td><a href="https://rnacentral.org/rna/URS0000C08F20/1080227">RS</a></td>
<td>0.986</td>
<td>0.929</td>
<td>-25.702</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PAM">=></a></td>
</tr>
<tr>
<td>CCDC59</td>
<td>5HSAA018576</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA018576/1">UTR</a></td>
<td>URS0000D8B901_1945864</td>
<td><a href="https://rnacentral.org/rna/URS0000D8B901/1945864">RS</a></td>
<td>0.957</td>
<td>0.978</td>
<td>-27.490</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CCDC59">=></a></td>
</tr>
<tr>
<td>ZNF780A</td>
<td>5HSAA123916</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123916/1">UTR</a></td>
<td>URS0000C39FD2_84024</td>
<td><a href="https://rnacentral.org/rna/URS0000C39FD2/84024">RS</a></td>
<td>0.971</td>
<td>0.972</td>
<td>-23.334</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF780A">=></a></td>
</tr>
<tr>
<td>XRCC4</td>
<td>5HSAA120464</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA120464/1">UTR</a></td>
<td>URS0000C5AB8F_218284</td>
<td><a href="https://rnacentral.org/rna/URS0000C5AB8F/218284">RS</a></td>
<td>0.986</td>
<td>0.940</td>
<td>-20.599</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/XRCC4">=></a></td>
</tr>
<tr>
<td>STYXL1</td>
<td>5HSAA105732</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA105732/1">UTR</a></td>
<td>URS0000BF519A_1295626</td>
<td><a href="https://rnacentral.org/rna/URS0000BF519A/1295626">RS</a></td>
<td>0.949</td>
<td>0.961</td>
<td>-31.588</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/STYXL1">=></a></td>
</tr>
<tr>
<td>LMLN</td>
<td>5HSAA059401</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA059401/1">UTR</a></td>
<td>URS00021EDEB6_1449351</td>
<td><a href="https://rnacentral.org/rna/URS00021EDEB6/1449351">RS</a></td>
<td>0.962</td>
<td>0.987</td>
<td>-10.299</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LMLN">=></a></td>
</tr>
<tr>
<td>UBL5</td>
<td>5HSAA116393</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA116393/1">UTR</a></td>
<td>URS0000C7BD69_1619069</td>
<td><a href="https://rnacentral.org/rna/URS0000C7BD69/1619069">RS</a></td>
<td>1.000</td>
<td>0.960</td>
<td>-49.906</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBL5">=></a></td>
</tr>
<tr>
<td>SMC4</td>
<td>5HSAA101371</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101371/1">UTR</a></td>
<td>URS0000D6A2DF_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6A2DF/12908">RS</a></td>
<td>1.000</td>
<td>0.978</td>
<td>-22.587</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SMC4">=></a></td>
</tr>
<tr>
<td>SEC24C</td>
<td>5HSAA095779</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095779/1">UTR</a></td>
<td>URS0000D7D0E9_867080</td>
<td><a href="https://rnacentral.org/rna/URS0000D7D0E9/867080">RS</a></td>
<td>0.998</td>
<td>0.921</td>
<td>-32.285</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SEC24C">=></a></td>
</tr>
<tr>
<td>HSD17B7</td>
<td>5HSAA051002</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA051002/1">UTR</a></td>
<td>URS0000D860F9_1971627</td>
<td><a href="https://rnacentral.org/rna/URS0000D860F9/1971627">RS</a></td>
<td>0.997</td>
<td>0.961</td>
<td>-40.631</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HSD17B7">=></a></td>
</tr>
<tr>
<td>UBAP2L</td>
<td>5HSAA115804</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115804/1">UTR</a></td>
<td>URS0000DA0EC8_431061</td>
<td><a href="https://rnacentral.org/rna/URS0000DA0EC8/431061">RS</a></td>
<td>0.988</td>
<td>0.966</td>
<td>-29.104</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UBAP2L">=></a></td>
</tr>
<tr>
<td>PPHLN1</td>
<td>5HSAA083267</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083267/1">UTR</a></td>
<td>URS0000C17D3E_1262955</td>
<td><a href="https://rnacentral.org/rna/URS0000C17D3E/1262955">RS</a></td>
<td>0.958</td>
<td>0.942</td>
<td>-40.381</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPHLN1">=></a></td>
</tr>
<tr>
<td>PIGF</td>
<td>5HSAA080186</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080186/1">UTR</a></td>
<td>URS0000AB977B_318586</td>
<td><a href="https://rnacentral.org/rna/URS0000AB977B/318586">RS</a></td>
<td>0.981</td>
<td>0.954</td>
<td>-38.068</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PIGF">=></a></td>
</tr>
<tr>
<td>RIPK4</td>
<td>5HSAA091137</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA091137/1">UTR</a></td>
<td>URS0000DA1909_1803447</td>
<td><a href="https://rnacentral.org/rna/URS0000DA1909/1803447">RS</a></td>
<td>0.951</td>
<td>0.982</td>
<td>-26.592</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RIPK4">=></a></td>
</tr>
<tr>
<td>RBMX2</td>
<td>5HSAA089726</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA089726/1">UTR</a></td>
<td>URS0000C41809_1262870</td>
<td><a href="https://rnacentral.org/rna/URS0000C41809/1262870">RS</a></td>
<td>0.982</td>
<td>0.953</td>
<td>-26.240</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RBMX2">=></a></td>
</tr>
<tr>
<td>RABGGTA</td>
<td>5HSAA087803</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA087803/1">UTR</a></td>
<td>URS0000C2E7A2_883113</td>
<td><a href="https://rnacentral.org/rna/URS0000C2E7A2/883113">RS</a></td>
<td>0.988</td>
<td>0.977</td>
<td>-31.731</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RABGGTA">=></a></td>
</tr>
<tr>
<td>TXNDC8</td>
<td>5HSAA115354</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA115354/1">UTR</a></td>
<td>URS0000D65E69_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D65E69/12908">RS</a></td>
<td>0.968</td>
<td>0.986</td>
<td>-12.866</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TXNDC8">=></a></td>
</tr>
<tr>
<td>PSMB3</td>
<td>5HSAA085508</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085508/1">UTR</a></td>
<td>URS0000C154E1_1105031</td>
<td><a href="https://rnacentral.org/rna/URS0000C154E1/1105031">RS</a></td>
<td>0.984</td>
<td>0.950</td>
<td>-30.643</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMB3">=></a></td>
</tr>
<tr>
<td>ALG13</td>
<td>5HSAA003869</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA003869/1">UTR</a></td>
<td>URS0000DB63E8_1341154</td>
<td><a href="https://rnacentral.org/rna/URS0000DB63E8/1341154">RS</a></td>
<td>0.995</td>
<td>0.982</td>
<td>-16.962</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ALG13">=></a></td>
</tr>
<tr>
<td>ASB3</td>
<td>5HSAA007257</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA007257/1">UTR</a></td>
<td>URS00023311D4_1895825</td>
<td><a href="https://rnacentral.org/rna/URS00023311D4/1895825">RS</a></td>
<td>0.951</td>
<td>0.901</td>
<td>-94.427</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ASB3">=></a></td>
</tr>
<tr>
<td>SEC23IP</td>
<td>5HSAA095755</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA095755/1">UTR</a></td>
<td>URS0000D9554A_1965562</td>
<td><a href="https://rnacentral.org/rna/URS0000D9554A/1965562">RS</a></td>
<td>1.000</td>
<td>0.973</td>
<td>-37.556</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SEC23IP">=></a></td>
</tr>
<tr>
<td>DDX27</td>
<td>5HSAA029048</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029048/1">UTR</a></td>
<td>URS0000C60D10_2340</td>
<td><a href="https://rnacentral.org/rna/URS0000C60D10/2340">RS</a></td>
<td>0.973</td>
<td>0.974</td>
<td>-21.548</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DDX27">=></a></td>
</tr>
<tr>
<td>GIN1</td>
<td>5HSAA044153</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA044153/1">UTR</a></td>
<td>URS000084D5C3_1507978</td>
<td><a href="https://rnacentral.org/rna/URS000084D5C3/1507978">RS</a></td>
<td>0.979</td>
<td>0.962</td>
<td>-27.270</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/GIN1">=></a></td>
</tr>
<tr>
<td>RPL21</td>
<td>5HSAA092442</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092442/1">UTR</a></td>
<td>URS0000D9CD14_1261545</td>
<td><a href="https://rnacentral.org/rna/URS0000D9CD14/1261545">RS</a></td>
<td>0.964</td>
<td>0.976</td>
<td>-10.586</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL21">=></a></td>
</tr>
<tr>
<td>FANCM</td>
<td>5HSAA039401</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA039401/1">UTR</a></td>
<td>URS0000C1822D_1503</td>
<td><a href="https://rnacentral.org/rna/URS0000C1822D/1503">RS</a></td>
<td>0.999</td>
<td>0.963</td>
<td>-41.136</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FANCM">=></a></td>
</tr>
<tr>
<td>LARP7</td>
<td>5HSAA057962</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA057962/1">UTR</a></td>
<td>URS0000AB6FB2_467705</td>
<td><a href="https://rnacentral.org/rna/URS0000AB6FB2/467705">RS</a></td>
<td>0.972</td>
<td>0.941</td>
<td>-30.747</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/LARP7">=></a></td>
</tr>
<tr>
<td>SHCBP1</td>
<td>5HSAA098020</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA098020/1">UTR</a></td>
<td>URS0000C0093C_75695</td>
<td><a href="https://rnacentral.org/rna/URS0000C0093C/75695">RS</a></td>
<td>0.970</td>
<td>0.980</td>
<td>-20.729</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SHCBP1">=></a></td>
</tr>
<tr>
<td>KIAA1143</td>
<td>5HSAA055963</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA055963/1">UTR</a></td>
<td>URS0000D8B0DB_405446</td>
<td><a href="https://rnacentral.org/rna/URS0000D8B0DB/405446">RS</a></td>
<td>0.967</td>
<td>0.968</td>
<td>-28.296</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/KIAA1143">=></a></td>
</tr>
<tr>
<td>MARK1</td>
<td>5HSAA063581</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA063581/1">UTR</a></td>
<td>URS0000AB38E1_754252</td>
<td><a href="https://rnacentral.org/rna/URS0000AB38E1/754252">RS</a></td>
<td>0.999</td>
<td>0.977</td>
<td>-12.858</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MARK1">=></a></td>
</tr>
<tr>
<td>DDX10</td>
<td>5HSAA028902</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA028902/1">UTR</a></td>
<td>URS0000DB3A77_2018041</td>
<td><a href="https://rnacentral.org/rna/URS0000DB3A77/2018041">RS</a></td>
<td>0.992</td>
<td>0.961</td>
<td>-24.228</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DDX10">=></a></td>
</tr>
<tr>
<td>PDK2</td>
<td>5HSAA078536</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA078536/1">UTR</a></td>
<td>URS00004D1143_305</td>
<td><a href="https://rnacentral.org/rna/URS00004D1143/305">RS</a></td>
<td>0.984</td>
<td>0.951</td>
<td>-51.650</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PDK2">=></a></td>
</tr>
<tr>
<td>CFHR3</td>
<td>5HSAA021322</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA021322/1">UTR</a></td>
<td>URS0000DB0E53_135739</td>
<td><a href="https://rnacentral.org/rna/URS0000DB0E53/135739">RS</a></td>
<td>0.976</td>
<td>0.954</td>
<td>-14.925</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CFHR3">=></a></td>
</tr>
<tr>
<td>XRCC5</td>
<td>5HSAA120483</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA120483/1">UTR</a></td>
<td>URS0000D91FFA_3562</td>
<td><a href="https://rnacentral.org/rna/URS0000D91FFA/3562">RS</a></td>
<td>0.995</td>
<td>0.965</td>
<td>-24.591</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/XRCC5">=></a></td>
</tr>
<tr>
<td>RICTOR</td>
<td>5HSAA091019</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA091019/1">UTR</a></td>
<td>URS0000E60855_1294143</td>
<td><a href="https://rnacentral.org/rna/URS0000E60855/1294143">RS</a></td>
<td>1.000</td>
<td>0.983</td>
<td>-19.704</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RICTOR">=></a></td>
</tr>
<tr>
<td>HOXA7</td>
<td>5HSAA050572</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050572/1">UTR</a></td>
<td>URS000232541F_1736411</td>
<td><a href="https://rnacentral.org/rna/URS000232541F/1736411">RS</a></td>
<td>0.994</td>
<td>0.938</td>
<td>-34.393</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXA7">=></a></td>
</tr>
<tr>
<td>PSMD6</td>
<td>5HSAA085666</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085666/1">UTR</a></td>
<td>URS0000C30169_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000C30169/12908">RS</a></td>
<td>0.988</td>
<td>0.988</td>
<td>-11.672</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMD6">=></a></td>
</tr>
<tr>
<td>EHF</td>
<td>5HSAA033773</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA033773/1">UTR</a></td>
<td>URS0000DAE44A_643674</td>
<td><a href="https://rnacentral.org/rna/URS0000DAE44A/643674">RS</a></td>
<td>0.921</td>
<td>0.957</td>
<td>-25.277</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/EHF">=></a></td>
</tr>
<tr>
<td>ALG13</td>
<td>5HSAA003878</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA003878/1">UTR</a></td>
<td>URS0000BFFD22_630626</td>
<td><a href="https://rnacentral.org/rna/URS0000BFFD22/630626">RS</a></td>
<td>0.961</td>
<td>0.953</td>
<td>-33.752</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ALG13">=></a></td>
</tr>
<tr>
<td>MCAT</td>
<td>5HSAA064155</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA064155/1">UTR</a></td>
<td>URS00021EDD5F_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDD5F/12908">RS</a></td>
<td>0.992</td>
<td>0.971</td>
<td>-29.600</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MCAT">=></a></td>
</tr>
<tr>
<td>CEPT1</td>
<td>5HSAA021163</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA021163/1">UTR</a></td>
<td>URS0002311D9E_1379858</td>
<td><a href="https://rnacentral.org/rna/URS0002311D9E/1379858">RS</a></td>
<td>0.986</td>
<td>0.941</td>
<td>-48.677</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CEPT1">=></a></td>
</tr>
<tr>
<td>PRSS27</td>
<td>5HSAA085280</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085280/1">UTR</a></td>
<td>URS0000AB1A13_257314</td>
<td><a href="https://rnacentral.org/rna/URS0000AB1A13/257314">RS</a></td>
<td>1.000</td>
<td>0.974</td>
<td>-14.802</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PRSS27">=></a></td>
</tr>
<tr>
<td>TMX2</td>
<td>5HSAA111796</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA111796/1">UTR</a></td>
<td>URS0000C3885A_1144310</td>
<td><a href="https://rnacentral.org/rna/URS0000C3885A/1144310">RS</a></td>
<td>0.994</td>
<td>0.940</td>
<td>-35.832</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TMX2">=></a></td>
</tr>
<tr>
<td>ZNF480</td>
<td>5HSAA123104</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA123104/1">UTR</a></td>
<td>URS0000ABB6D4_1002809</td>
<td><a href="https://rnacentral.org/rna/URS0000ABB6D4/1002809">RS</a></td>
<td>0.956</td>
<td>0.978</td>
<td>-28.578</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZNF480">=></a></td>
</tr>
<tr>
<td>OSBPL2</td>
<td>5HSAA075443</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA075443/1">UTR</a></td>
<td>URS0000D6B996_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D6B996/12908">RS</a></td>
<td>0.986</td>
<td>0.975</td>
<td>-11.592</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/OSBPL2">=></a></td>
</tr>
<tr>
<td>MRPL36</td>
<td>5HSAA067456</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA067456/1">UTR</a></td>
<td>URS000043D886_326424</td>
<td><a href="https://rnacentral.org/rna/URS000043D886/326424">RS</a></td>
<td>0.963</td>
<td>0.967</td>
<td>-25.410</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/MRPL36">=></a></td>
</tr>
<tr>
<td>SPG11</td>
<td>5HSAA103257</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA103257/1">UTR</a></td>
<td>URS0000E60183_1561204</td>
<td><a href="https://rnacentral.org/rna/URS0000E60183/1561204">RS</a></td>
<td>0.976</td>
<td>0.984</td>
<td>-15.250</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPG11">=></a></td>
</tr>
<tr>
<td>PPIA</td>
<td>5HSAA083307</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083307/1">UTR</a></td>
<td>URS0000C72892_999898</td>
<td><a href="https://rnacentral.org/rna/URS0000C72892/999898">RS</a></td>
<td>0.982</td>
<td>0.968</td>
<td>-31.876</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPIA">=></a></td>
</tr>
<tr>
<td>HOXB5</td>
<td>5HSAA050586</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050586/1">UTR</a></td>
<td>URS0000DA4E88_1214604</td>
<td><a href="https://rnacentral.org/rna/URS0000DA4E88/1214604">RS</a></td>
<td>0.990</td>
<td>0.975</td>
<td>-7.999</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXB5">=></a></td>
</tr>
<tr>
<td>SMU1</td>
<td>5HSAA101610</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101610/1">UTR</a></td>
<td>URS0000DAA552_1937003</td>
<td><a href="https://rnacentral.org/rna/URS0000DAA552/1937003">RS</a></td>
<td>0.956</td>
<td>0.918</td>
<td>-42.756</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SMU1">=></a></td>
</tr>
<tr>
<td>ST14</td>
<td>5HSAA104180</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA104180/1">UTR</a></td>
<td>URS0000D85B45_1686310</td>
<td><a href="https://rnacentral.org/rna/URS0000D85B45/1686310">RS</a></td>
<td>0.990</td>
<td>0.983</td>
<td>-10.358</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ST14">=></a></td>
</tr>
<tr>
<td>C1D</td>
<td>5HSAA013475</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA013475/1">UTR</a></td>
<td>URS00021EDC92_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDC92/12908">RS</a></td>
<td>0.987</td>
<td>0.975</td>
<td>-22.354</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C1D">=></a></td>
</tr>
<tr>
<td>C1D</td>
<td>5HSAA013479</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA013479/1">UTR</a></td>
<td>URS0000C3D875_520764</td>
<td><a href="https://rnacentral.org/rna/URS0000C3D875/520764">RS</a></td>
<td>0.969</td>
<td>0.961</td>
<td>-26.396</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/C1D">=></a></td>
</tr>
<tr>
<td>PPIC</td>
<td>5HSAA083329</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA083329/1">UTR</a></td>
<td>URS0000D82E1C_570947</td>
<td><a href="https://rnacentral.org/rna/URS0000D82E1C/570947">RS</a></td>
<td>0.959</td>
<td>0.944</td>
<td>-17.196</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PPIC">=></a></td>
</tr>
<tr>
<td>AUH</td>
<td>5HSAA009015</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA009015/1">UTR</a></td>
<td>URS0000C24AC0_1508404</td>
<td><a href="https://rnacentral.org/rna/URS0000C24AC0/1508404">RS</a></td>
<td>0.991</td>
<td>0.933</td>
<td>-33.610</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/AUH">=></a></td>
</tr>
<tr>
<td>HNRNPH1</td>
<td>5HSAA050023</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050023/1">UTR</a></td>
<td>URS0000BEBE94_1314783</td>
<td><a href="https://rnacentral.org/rna/URS0000BEBE94/1314783">RS</a></td>
<td>0.972</td>
<td>0.947</td>
<td>-62.380</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HNRNPH1">=></a></td>
</tr>
<tr>
<td>RPL9</td>
<td>5HSAA092644</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092644/1">UTR</a></td>
<td>URS0000D669BC_12908</td>
<td><a href="https://rnacentral.org/rna/URS0000D669BC/12908">RS</a></td>
<td>0.982</td>
<td>0.976</td>
<td>-19.430</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPL9">=></a></td>
</tr>
<tr>
<td>UQCRQ</td>
<td>5HSAA117212</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA117212/1">UTR</a></td>
<td>URS0000D7F295_1679721</td>
<td><a href="https://rnacentral.org/rna/URS0000D7F295/1679721">RS</a></td>
<td>0.996</td>
<td>0.970</td>
<td>-34.119</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/UQCRQ">=></a></td>
</tr>
<tr>
<td>CUL3</td>
<td>5HSAA027204</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA027204/1">UTR</a></td>
<td>URS0000AB1F37_697284</td>
<td><a href="https://rnacentral.org/rna/URS0000AB1F37/697284">RS</a></td>
<td>0.999</td>
<td>0.954</td>
<td>-34.144</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/CUL3">=></a></td>
</tr>
<tr>
<td>DYNC1LI1</td>
<td>5HSAA032829</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA032829/1">UTR</a></td>
<td>URS0000DAF156_573497</td>
<td><a href="https://rnacentral.org/rna/URS0000DAF156/573497">RS</a></td>
<td>0.979</td>
<td>0.961</td>
<td>-49.730</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DYNC1LI1">=></a></td>
</tr>
<tr>
<td>FTSJ1</td>
<td>5HSAA042042</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA042042/1">UTR</a></td>
<td>URS000231584D_1321816</td>
<td><a href="https://rnacentral.org/rna/URS000231584D/1321816">RS</a></td>
<td>0.953</td>
<td>0.975</td>
<td>-17.594</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/FTSJ1">=></a></td>
</tr>
<tr>
<td>RPS24</td>
<td>5HSAA092962</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092962/1">UTR</a></td>
<td>URS000231AF1A_1519493</td>
<td><a href="https://rnacentral.org/rna/URS000231AF1A/1519493">RS</a></td>
<td>0.995</td>
<td>0.954</td>
<td>-31.809</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS24">=></a></td>
</tr>
<tr>
<td>ENY2</td>
<td>5HSAA035639</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA035639/1">UTR</a></td>
<td>URS0000D8B865_1317112</td>
<td><a href="https://rnacentral.org/rna/URS0000D8B865/1317112">RS</a></td>
<td>0.991</td>
<td>0.969</td>
<td>-30.696</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ENY2">=></a></td>
</tr>
<tr>
<td>BNIP2</td>
<td>5HSAA010809</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA010809/1">UTR</a></td>
<td>URS0000D8C24D_1118156</td>
<td><a href="https://rnacentral.org/rna/URS0000D8C24D/1118156">RS</a></td>
<td>0.967</td>
<td>0.965</td>
<td>-47.901</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BNIP2">=></a></td>
</tr>
<tr>
<td>ZFR2</td>
<td>5HSAA121708</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA121708/1">UTR</a></td>
<td>URS0000C7BA37_1679168</td>
<td><a href="https://rnacentral.org/rna/URS0000C7BA37/1679168">RS</a></td>
<td>0.976</td>
<td>0.940</td>
<td>-9.935</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/ZFR2">=></a></td>
</tr>
<tr>
<td>PSMD6</td>
<td>5HSAA085677</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA085677/1">UTR</a></td>
<td>URS0000C017D4_935700</td>
<td><a href="https://rnacentral.org/rna/URS0000C017D4/935700">RS</a></td>
<td>0.991</td>
<td>0.985</td>
<td>-16.518</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PSMD6">=></a></td>
</tr>
<tr>
<td>HOXB7</td>
<td>5HSAA050591</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA050591/1">UTR</a></td>
<td>URS0002321CD3_1206781</td>
<td><a href="https://rnacentral.org/rna/URS0002321CD3/1206781">RS</a></td>
<td>0.997</td>
<td>0.945</td>
<td>-18.796</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/HOXB7">=></a></td>
</tr>
<tr>
<td>PIGF</td>
<td>5HSAA080173</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA080173/1">UTR</a></td>
<td>URS0000D7D2E6_1382803</td>
<td><a href="https://rnacentral.org/rna/URS0000D7D2E6/1382803">RS</a></td>
<td>0.996</td>
<td>0.977</td>
<td>-9.686</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/PIGF">=></a></td>
</tr>
<tr>
<td>WBP11</td>
<td>5HSAA119059</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA119059/1">UTR</a></td>
<td>URS0002328E56_1418104</td>
<td><a href="https://rnacentral.org/rna/URS0002328E56/1418104">RS</a></td>
<td>0.972</td>
<td>0.932</td>
<td>-31.378</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/WBP11">=></a></td>
</tr>
<tr>
<td>SMU1</td>
<td>5HSAA101609</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA101609/1">UTR</a></td>
<td>URS0000AB4909_367336</td>
<td><a href="https://rnacentral.org/rna/URS0000AB4909/367336">RS</a></td>
<td>0.966</td>
<td>0.944</td>
<td>-41.608</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SMU1">=></a></td>
</tr>
<tr>
<td>DDX27</td>
<td>5HSAA029046</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA029046/1">UTR</a></td>
<td>URS00021EDB97_12908</td>
<td><a href="https://rnacentral.org/rna/URS00021EDB97/12908">RS</a></td>
<td>0.989</td>
<td>0.991</td>
<td>-5.801</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DDX27">=></a></td>
</tr>
<tr>
<td>DLGAP1</td>
<td>5HSAA030613</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA030613/1">UTR</a></td>
<td>URS0000AB7CB8_122586</td>
<td><a href="https://rnacentral.org/rna/URS0000AB7CB8/122586">RS</a></td>
<td>0.986</td>
<td>0.979</td>
<td>-4.016</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/DLGAP1">=></a></td>
</tr>
<tr>
<td>RPS14</td>
<td>5HSAA092865</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA092865/1">UTR</a></td>
<td>URS0000ABA99F_621372</td>
<td><a href="https://rnacentral.org/rna/URS0000ABA99F/621372">RS</a></td>
<td>0.976</td>
<td>0.942</td>
<td>-17.490</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/RPS14">=></a></td>
</tr>
<tr>
<td>TTPAL</td>
<td>5HSAA114956</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA114956/1">UTR</a></td>
<td>URS0002313BB3_1906740</td>
<td><a href="https://rnacentral.org/rna/URS0002313BB3/1906740">RS</a></td>
<td>0.989</td>
<td>0.970</td>
<td>-60.727</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/TTPAL">=></a></td>
</tr>
<tr>
<td>SPATA19</td>
<td>5HSAA102982</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA102982/1">UTR</a></td>
<td>URS0000E5FC23_1484158</td>
<td><a href="https://rnacentral.org/rna/URS0000E5FC23/1484158">RS</a></td>
<td>0.932</td>
<td>0.976</td>
<td>-10.885</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/SPATA19">=></a></td>
</tr>
<tr>
<td>BTG2</td>
<td>5HSAA011301</td>
<td><a href="http://utrdb.ba.itb.cnr.it/getutr/5HSAA011301/1">UTR</a></td>
<td>URS0000C70E90_1127131</td>
<td><a href="https://rnacentral.org/rna/URS0000C70E90/1127131">RS</a></td>
<td>0.973</td>
<td>0.971</td>
<td>-28.246</td>
<td><a href="/human_riboswitch_hits_gallery/_mds/BTG2">=></a></td>
</tr>
</tbody>
</table>