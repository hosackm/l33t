const std = @import("std");

fn ch_to_idx(ch: u8) usize {
    return @as(usize, ch - 'a');
}

pub fn can_construct(letter: []const u8, magazine: []const u8) bool {
    var letter_count: [26]u8 = std.mem.zeroes([26]u8);
    var magazine_count: [26]u8 = std.mem.zeroes([26]u8);

    for (letter) |ch| {
        letter_count[ch_to_idx(ch)] += 1;
    }

    for (magazine) |ch| {
        magazine_count[ch_to_idx(ch)] += 1;
    }

    for (letter) |ch| {
        if (letter_count[ch_to_idx(ch)] > magazine_count[ch_to_idx(ch)]) {
            return false;
        }
    }

    return true;
}

test "can_construct" {
    try std.testing.expect(can_construct("a", "b") == false);
    try std.testing.expect(can_construct("aa", "ab") == false);
    try std.testing.expect(can_construct("aa", "aab") == true);
}
