from django import forms

class TorrentForm(forms.Form):
    torrent_list = forms.CharField(label='Enter list of torrent URLs on separate lines',
                                   widget=forms.Textarea,
                                   strip=True)
