import mne

# Reads from edf file
raw = mne.io.read_raw_edf("dreamsessions_night_12_2014_march_30.edf")
# We need to implement this part depending on the playback.ini content
# (channels depending on setup of recording)
# Sets the good channels for eMotiv
ch_names=[u'AF3', u'F7', u'F3', u'FC5', u'T7',
            u'P7', u'O1', u'O2', u'P8', u'T8', u'FC6', u'F4', u'F8', u'AF4']
# Sets the bad channels for eMotiv
# we need to remove the stim014 from bads later
bads = [u'COUNTER', u'INTERPOLATED', u'RAW_CQ', u'CQ_AF3', u'CQ_F7', u'CQ_F3',
        u'CQ_FC5', u'CQ_T7', u'CQ_P7', u'CQ_O1', u'CQ_O2', u'CQ_P8', u'CQ_T8',
        u'CQ_FC6', u'CQ_F4', u'CQ_F8', u'CQ_AF4', u'CQ_CMS', u'CQ_DRL',
        u'GYROX', u'GYROY', 'STI 014']
# Set sfreq for eMotiv
sfreq = 128
"""
print raw.ch_names
print raw.info
"""
picks = mne.pick_channels(ch_names = raw.ch_names, include=ch_names, exclude=bads)
print picks
# Give sample index from time index
start, stop = raw.time_as_index([0, 1])
# Here we define a number of sample for the buffer to output based on the
# eMotiv sfreq : 1/8second
stop = 16
# Then we select the corresponding chunk of data
data, times = raw[picks, start:(stop + 1)]
print data
"""
info = mne.create_info(sfreq=sfreq, ch_names=ch_names, ch_types='eeg')
"""
while 1:
    data, times = raw[picks, start:(stop + 1)]
    print data
    start += stop + 1
    if (start ==)
        start = 0
    sleep(0.125)
