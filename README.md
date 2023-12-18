# cs105-mlprivacy

## Code Description

## Project Description

**Technical Component** 

Machine learning models are often trained on highly sensitive data. Sometimes, the learned structure of the models can encode information that, if extracted, would be harmful to certain individuals or groups. An interesting technical problem that arises, then, is how can we ensure that ML models themselves are robust to data privacy concerns?

There are several standards which have been put forth in the literature. In this project, we’ll focus on the techniques described by Xiao and Devadas in their Probably Approximately Correct (PAC) approach. The authors outline several algorithms that upper bound inference of training input. More specifically, the authors determine the minimum noise needed in various learning scenarios to restrict the ability of a malicious agent to infer training data, while maintaining decent performance. The thesis of the paper is that the privacy standard put forth by differential privacy (model trained on dataset D vs model trained on dataset D-x should be indistinguishable), is too harsh/leads to unnecessary loss in performance. The standard put forth by PAC privacy (no individual’s data can be reconstructed), is sufficient, and also leads to significant improvements in performance.

For the technical component of our project, we will 1) implement at least one algorithm outlined in the PAC paper and 2) summarize the algorithm in layman terms. 

**Policy Component**

This project will also include a policy/legal component in the form of an analytical paper. We would examine the legal applications of copyright for machine learning, including whether machine learning models and their outputs can be copyrighted, the legal implications of using copyright images to train ML models, and whether AI generated versions of copyrighted images and artwork violate copyright. While courts have ruled that AI-generated images cannot be copyrighted, legal lines begin to blur when AI is used to assist humans in the creation of work. What is the threshold of human involvement required to produce copyright? How can courts infer whether a work is human or AI generated? Should disclosure of AI use be required, even if the machine learning model was created and trained entirely independently by the individual who produced the work? 

This ties into the technical component of our project as follows: we will argue that meeting the privacy standard put forth by PAC privacy is also sufficient to meet the requirements of copyright law, both in terms of the current legal standard and from an ethical standpoint. In other words, we will discuss the parallels between protecting the privacy of training data consisting of images of humans and protecting the copyright of training images (ex artworks) used in the generation of images. This expands upon the intersection of privacy and property in copyright law. 

## Source Description