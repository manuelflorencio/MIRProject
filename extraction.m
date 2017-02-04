clear all;


cd('Benetos')

% Inputs:
%  filename filename for .wav file
%  iter     number of iterations (e.g. 30)
%  S        number of sources (e.g. 3)
%  sz       sparsity parameter for pitch activation (e.g. 1.0-1.3)
%  su       sparsity parameter for source contribution (e.g. 1.0-1.3)
%  sh       sparsity parameter for pitch shifting (e.g. 1.0-1.3)
%
% Outputs:
%  pianoRoll raw piano-roll output (dims: P x T, P: pitch index, T: 20ms step)

filename_audio = strcat(pwd, '\Dataset\Saarland\Bach_BWV849-01_001_20090916-smd.mp3');
filename_mid = strcat(pwd, '\Dataset\Saarland\Bach_BWV849-01_001_20090916-smd.mid');

iter = 30;
S = 3;
sz = 1;
su = 1;
sh = 1;

[benetosResults] = transcription(filename_audio,iter,S,sz,su,sh);


cd('..')
cd('evaluation')

%Save the output in a file
csvwrite('dataBenetos.txt',benetosResults);

cd('..')


%%Second step, run the Klaputi's code which is in Essentia%%
cd('Klapuri')
%%Make python code to use the code of Klapuri and save the results in a
%%file

!python extraction_klapuri.py

cd('..')


%%Third step, run the code to evaluate
cd('evaluation')
%%Python code to evaluate the results of the files with the ground truth
%%http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
!python evaluation.py

cd('..')
