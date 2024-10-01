
SISI-P  (Scrambled Image Segments Interconnection Protocol) 
---
Author: ياسر ابو ياسمين عمارة ٦ + ٣٠

**Description**:  
---

Through scattered shards of data you’ll glide,  
Where SISI-P’s riddles and fragments reside.  
Find the order hidden deep in the flow,  
Piece by piece, the picture will show.

Follow the clues, no segment’s too small,  
Unveil the image, and you’ll have it all.  
When the puzzle is clear, the flag will arise,  
A prize for those with discerning eyes.

_Note: Place the Lua dissector in_  
`C:\Program Files\Wireshark\plugins`

**Solution**:  
---
-   **Install the Lua Dissector**: Participants must place the Lua dissector in `C:\Program Files\Wireshark\plugins` to decode the SISI-P protocol.
    
-   **Use Segment IDs**: Once decoded, participants will need to use the segment IDs in the packet data to correctly reassemble the image.
    
-   **Extract the Flag**: The reassembled image contains the flag.

Flag
---
```
PlaygroundsCTF{here_kitty_kitty}
```