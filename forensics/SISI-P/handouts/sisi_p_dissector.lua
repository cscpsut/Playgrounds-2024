-- Add this line at the very beginning of the file
package.path = package.path .. ";C:\\Program Files\\Wireshark\\plugins\\?.lua"

-- The rest of your script follows
local util = require("util")

-- ... rest of the script content ...
-- Define the protocol
local sisi_p_proto = Proto("SISI-P", "Scrambled Image Segments Interconnection Protocol")

-- Define protocol fields
local f_packet_type = ProtoField.uint8("sisip.packet_type", "Packet Type", base.DEC)
local f_sequence_number = ProtoField.uint16("sisip.sequence_number", "Sequence Number", base.DEC)
local f_segment_id = ProtoField.uint16("sisip.segment_id", "Segment ID (Hidden)", base.HEX)
local f_total_segments = ProtoField.uint16("sisip.total_segments", "Total Segments", base.DEC)
local f_data_length = ProtoField.uint16("sisip.data_length", "Data Length", base.DEC)
local f_image_data = ProtoField.bytes("sisip.image_data", "Image Data")

-- Define expert info
local expert_note = ProtoExpert.new("sisip.comment", "SISI-P Comment", expert.group.COMMENTS, expert.severity.COMMENT)

sisi_p_proto.fields = {f_packet_type, f_sequence_number, f_segment_id, f_total_segments, f_data_length, f_image_data}
sisi_p_proto.experts = {expert_note}

-- Dissector function
function sisi_p_proto.dissector(buffer, pinfo, tree)
    local length = buffer:len()
    if length == 0 then return end

    pinfo.cols.protocol = sisi_p_proto.name

    -- Create a subtree for the protocol
    local subtree = tree:add(sisi_p_proto, buffer(), "SISI-P Data")

    -- Add fields to the subtree
    subtree:add(f_packet_type, buffer(0,1))
    subtree:add(f_sequence_number, buffer(1,2))
    
    -- Only display the segment ID if the Lua script is loaded
    local segment_id_subtree = subtree:add(f_segment_id, buffer(3,2))
    segment_id_subtree:set_text("Segment ID (Hidden): " .. buffer(3,2):uint())
    segment_id_subtree:add_proto_expert_info(expert_note, "Segment ID is key for reconstructing the image. Only viewable with Lua script.")

    subtree:add(f_total_segments, buffer(5,2))
    subtree:add(f_data_length, buffer(7,2))
    
    local data_length = buffer(7,2):uint()
    local image_data = buffer(9, data_length)
    subtree:add(f_image_data, image_data)
end

-- Register the dissector
local udp_port = 8888  -- Replace with the actual port number used by SISI-P
local udp_dissector_table = DissectorTable.get("udp.port")
udp_dissector_table:add(udp_port, sisi_p_proto)