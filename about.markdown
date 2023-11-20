---
layout: page
title: About
permalink: /about/
---


## Abstract

Riboswitches are a class of noncoding RNA structures that interact with target ligands to cause a conformational change that can then execute some regulatory purpose within the cell. Riboswitches are ubiquitous and well characterized in bacteria, with additional examples also being found in fungi, plants, and yeast. To date, no purely RNA-small molecule riboswitch has been discovered in  *Homo Sapiens*. Several analogous riboswitch-like mechanisms have been described within the *H. Sapiens* translatome within the past decade, prompting the question: Is there a *H. Sapiens* riboswitch dependent on only small molecule ligands? In this work, we trained positive-unlabeled machine learning classifiers on known riboswitch sequences and apply the classifiers to *H. Sapiens* mRNA 5’ 5'UTR sequences found in the 5'UTR database, UTRdb, in the hope of identifying a set of mRNAs to investigate for riboswitch functionality. 67,683 riboswitch sequences were obtained from RNAcentral and sorted for ligand type and used as positive examples and 48,031 5'UTR sequences were used as unlabeled, unknown examples.
Positive examples were sorted by ligand, and 20 positive-unlabeled classifiers were trained on sequence and secondary structure features while withholding one or two ligand classes. Cross validation was then performed on the withheld ligand sets to obtain a validation accuracy range of 75\%-99\%. The joint sets of 5'UTRs identified as potential riboswitches by the 20 classifiers were then analyzed. 1515 sequences were identified as a riboswitch by one or more classifier(s) and 436 of the *H. Sapiens* 5'UTRs were labeled as harboring potential riboswitch elements by all 20 classifiers. These 436 sequences were mapped back to the most similar riboswitches within the positive data and examined. An online database of identified and ranked 5'UTRs, their features, and their most similar matches to known riboswitches, is provided to guide future experimental efforts to identify *H. Sapiens* riboswitches

## How to use the website


![](../table_explaination.png?raw=true)

![](../Figure5.png?raw=true)

## Contact info

#### William S. Raymond<sup>1,&</sup>, Jacob DeRoo<sup>1</sup>, Brian Munsky<sup>1,2,$</sup>

<sup><sup>1</sup> School of Biomedical Engineering, Colorado State University Fort Collins, CO 80523, USA</sup>
<sup><sup>2</sup>  Chemical and Biological Engineering, Colorado State University Fort Collins, CO 80523, USA</sup>

& <a href="wsraymon@rams.colostate.edu">wsraymon@rams.colostate.edu</a>

$ <a href="brian.munsky@colostate.edu">brian.munsky@colostate.edu</a> 

## Table links

[Link to Ensemble of 20 table](../display_436)

[Link to Ensemble of 1 table](../display_1533)
