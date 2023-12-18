# cs105-mlprivacy

## Code Description

We implement Algorithm 1: (1-gamma)-Confidence Noise Determination of Deterministic Mechanism M from https://arxiv.org/abs/2210.03458, Section 4.1: Deterministic Mechanism

Algorithm 1 determines the Gaussian noise needed to achieve a specified upper bound on mutual information with high confidence for a given deterministic mechanism M. Mutual information (MI) is the statistical dependence (information shared) between two random variables (in this case, model input and model output). Bounding mutual information, and thus bounding an adverary's ability to reconstruct sensitive training data given model output, is a very important problem in Machine Learning.

The steps of Algorithm 1 are as follows:

1. Generate data samples X_1, ..., X_m
2. Record M(X_i) for all X
3. Compute the empirical Covariance Matrix on X, M
4. Estimate the added noise required to preserve MI. Specifically, compute the covariance matrix for some added noise B such that MI(X; M(X) + B) is upper bounded as required.

The algorithm determines the noise covariance matrix based on the eigenvalue gap. The implementation takes into account cases where the eigenvalues of the covariance matrix are distinct or when a more pessimistic perturbation is required, adjusting the noise parameters accordingly. The goal is to provide a rigorous approach to privacy-preserving mechanisms by introducing Gaussian noise and enabling control over information leakage in a provable manner.

In summary, the implemented Algorithm 1 successfully estimates the necessary added noise required to achieve a desired upper bound on mutual information for a given deterministic mechanism. The approach considers the eigenvalue structure of the empirical covariance matrix, allowing for different noise perturbations based on the eigenvalue gap. The resulting implementation provides a systematic and confidence-driven approach to ensuring privacy in scenarios where deterministic mechanisms are employed, contributing to a comprehensive understanding of information leakage control in practical applications.

## Project Description

**Technical Component** 

Machine learning models are often trained on highly sensitive data. Sometimes, the learned structure of the models can encode information that, if extracted, would be harmful to certain individuals or groups. An interesting technical problem that arises, then, is how can we ensure that ML models themselves are robust to data privacy concerns?

There are several standards which have been put forth in the literature. In this project, we’ll focus on the techniques described by Xiao and Devadas in their Probably Approximately Correct (PAC) approach. The authors outline several algorithms that upper bound inference of training input. More specifically, the authors determine the minimum noise needed in various learning scenarios to restrict the ability of a malicious agent to infer training data, while maintaining decent performance. The thesis of the paper is that the privacy standard put forth by differential privacy (model trained on dataset D vs model trained on dataset D-x should be indistinguishable), is too harsh/leads to unnecessary loss in performance. The standard put forth by PAC privacy (no individual’s data can be reconstructed), is sufficient, and also leads to significant improvements in performance.

For the technical component of our project, we will 1) implement at least one algorithm outlined in the PAC paper and 2) summarize the algorithm in layman terms. 

**Policy Component**

This project will also include a policy/legal component in the form of an analytical paper. We would examine the legal applications of copyright for machine learning, including whether machine learning models and their outputs can be copyrighted, the legal implications of using copyright images to train ML models, and whether AI generated versions of copyrighted images and artwork violate copyright. While courts have ruled that AI-generated images cannot be copyrighted, legal lines begin to blur when AI is used to assist humans in the creation of work. What is the threshold of human involvement required to produce copyright? How can courts infer whether a work is human or AI generated? Should disclosure of AI use be required, even if the machine learning model was created and trained entirely independently by the individual who produced the work? 

This ties into the technical component of our project as follows: we will argue that meeting the privacy standard put forth by PAC privacy is also sufficient to meet the requirements of copyright law, both in terms of the current legal standard and from an ethical standpoint. In other words, we will discuss the parallels between protecting the privacy of training data consisting of images of humans and protecting the copyright of training images (ex artworks) used in the generation of images. This expands upon the intersection of privacy and property in copyright law. 

## Recommended Reading

We have attached excerpts from both the paper we followed for this work and an article written about this work. We recommend reading these excerpts to gain additional understanding of the project subject matter. 

**Introduction to "A New Way to Look at Data Privacy", a review of the PAC Paper**

Imagine that a team of scientists has developed a machine-learning model that can predict whether a patient has cancer from lung scan images. They want to share this model with hospitals around the world so clinicians can start using it in diagnosis.

But there’s a problem. To teach their model how to predict cancer, they showed it millions of real lung scan images, a process called training. Those sensitive data, which are now encoded into the inner workings of the model, could potentially be extracted by a malicious agent. The scientists can prevent this by adding noise, or more generic randomness, to the model that makes it harder for an adversary to guess the original data. However, perturbation reduces a model’s accuracy, so the less noise one can add, the better.

MIT researchers have developed a technique that enables the user to potentially add the smallest amount of noise possible, while still ensuring the sensitive data are protected.

The researchers created a new privacy metric, which they call Probably Approximately Correct (PAC) Privacy, and built a framework based on this metric that can automatically determine the minimal amount of noise that needs to be added. Moreover, this framework does not need knowledge of the inner workings of a model or its training process, which makes it easier to use for different types of models and applications.

In several cases, the researchers show that the amount of noise required to protect sensitive data from adversaries is far less with PAC Privacy than with other approaches. This could help engineers create machine-learning models that provably hide training data, while maintaining accuracy in real-world settings.

“PAC Privacy exploits the uncertainty or entropy of the sensitive data in a meaningful way,  and this allows us to add, in many cases, an order of magnitude less noise. This framework allows us to understand the characteristics of arbitrary data processing and privatize it automatically without artificial modifications. While we are in the early days and we are doing simple examples, we are excited about the promise of this technique,” says Srini Devadas, the Edwin Sibley Webster Professor of Electrical Engineering and co-author of a new paper on PAC Privacy.

Source: “A New Way to Look at Data Privacy.” MIT News | Massachusetts Institute of Technology, 14 July 2023, https://news.mit.edu/2023/new-way-look-data-privacy-0714.

**Introduction to Section 4: Automatic Control of Mutual Information from the PAC Paper: https://arxiv.org/abs/2210.03458**

In this section, we present our main results on automatic privacy measurement and control. At a high level, we want an automatic protocol which takes security parameters as input and returns a privatization scheme on M to ensure required privacy guarantees with high confidence. In particular, we want the least assumptions on mechanism M, which ideally could be a black-box oracle and no specific algorithmic analysis is needed to produce the security proof.
One natural idea to achieve information leakage control is perturbation: when MI(X;M(X)) is not small enough to produce satisfied PAC Privacy, we may add additional noise B, say Gaussian, to produce smaller MI(X;M(X)+B). In PAC Privacy, the role of noise is not simply perturbation but to also enforce the output of a black-box oracle into a class of parameterized distributions. As shown below for either deterministic or randomized algorithms, with Gaussian noise, the analysis is reduced to the study of divergences of Gaussian
mixture models. The key question left is how to automatically determine the parameters of the noise B. We give solutions in this section. In Section 4.1, we focus on the deterministic M(·) w.r.t. X, while, in Section 4.2, we analyze generic randomized M(·) w.r.t either X or a single datapoint x_i. Finally, in Section 4.3, we discuss how to approximate the optimal perturbation.

Source: Hanshen Xiao and Srinivas Devadas. PAC Privacy: Automatic Privacy Measurement and Control of Data Processing. arXiv e-prints,art. arXiv:2210.03458, October 2022. doi: 10.48550/arXiv.2210. 03458.