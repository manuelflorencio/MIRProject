function freq = midi2freq(midiNote)
    % Converts midiNote to a frequency in Hz
    if isempty(midiNote)
        freq = [];
    else
        freq =(440/32)*2.^((midiNote-9)/12).*(midiNote>0);
    end
end