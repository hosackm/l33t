const std = @import("std");

fn match(ch: u8) u8 {
    return switch (ch) {
        '}' => '{',
        ')' => '(',
        ']' => '[',
        else => '!',
    };
}

pub fn is_valid(s: []const u8) bool {
    if (s.len % 2 != 0) {
        return false;
    }

    var stack = std.ArrayList(u8).init(std.heap.page_allocator);
    defer stack.deinit();

    for (s) |ch| {
        switch (ch) {
            '{', '(', '[' => stack.append(ch) catch return false,
            '}', ')', ']' => {
                if (stack.items.len == 0 or stack.pop() != match(ch)) {
                    return false;
                }
            },
            else => return false,
        }
    }

    return stack.items.len == 0;
}

test "is valid with basic examples" {
    try std.testing.expect(is_valid("()") == true);
    try std.testing.expect(is_valid("()[]{}") == true);
    try std.testing.expect(is_valid("(]") == false);
}
