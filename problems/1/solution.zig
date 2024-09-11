const std = @import("std");

pub fn two_sum(nums: []const i32, target: i32) ![2]usize {
    var alloc = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = alloc.deinit();
    var table = std.AutoHashMap(i32, usize).init(alloc.allocator());
    defer table.deinit();

    for (nums, 0..) |n, i| {
        const compliment = target - n;
        if (table.get(compliment)) |index| {
            return .{ index, i };
        }
        try table.put(n, i);
    }

    return error.NoSolutionPossible;
}

test "test two sum 1" {
    const inputs = [_]i32{ 2, 7, 11, 15 };
    const target: i32 = 9;
    const expected = [_]usize{ 0, 1 };

    const answer = try two_sum(&inputs, target);
    try std.testing.expect(std.mem.eql(usize, &answer, &expected));
}

test "test two sum 2" {
    const inputs = [_]i32{ 3, 2, 4 };
    const target: i32 = 6;
    const expected = [_]usize{ 1, 2 };

    const answer = try two_sum(&inputs, target);
    try std.testing.expect(std.mem.eql(usize, &answer, &expected));
}

test "test two sum 3" {
    const inputs = [_]i32{ 3, 3 };
    const target: i32 = 6;
    const expected = [_]usize{ 0, 1 };

    const answer = try two_sum(&inputs, target);
    try std.testing.expect(std.mem.eql(usize, &answer, &expected));
}
