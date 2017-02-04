clear all

%%First step, extract all f0s for Saarland MIDI dataset.
s = dir('Dataset\Saarland\*.mid');
a = cellstr(strvcat(s.name));
for i=1:length(a)
    miditofreq('Dataset\Saarland\', 'evaluation\Saarland\', a{i});
end
