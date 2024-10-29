fn get_area(h: []const i32, l: usize, r: usize) i32 {
    const height = @min(h[l], h[r]);
    return height * @as(i32, @intCast(r - l));
}

fn max_area(heights: []const i32) i32 {
    var left: usize = 0;
    var right: usize = heights.len - 1;
    var max: i32 = 0;

    while (left < right) {
        const area = get_area(heights, left, right);
        if (area > max) {
            max = area;
        }
        if (heights[left] < heights[right]) {
            left += 1;
        } else {
            right -= 1;
        }
    }

    return max;
}

test "leetcode examples" {
    const expect = @import("std").testing.expect;

    try expect(max_area(&[_]i32{ 1, 8, 6, 2, 5, 4, 8, 3, 7 }) == 49);
    try expect(max_area(&[_]i32{ 1, 1 }) == 1);
    try expect(max_area(&[_]i32{ 1, 2, 4, 3 }) == 4);
    try expect(max_area(&[_]i32{ 2, 3, 4, 5, 18, 17, 6 }) == 17);
    try expect(max_area(&[_]i32{ 1, 0, 0, 0, 0, 0, 0, 2, 2 }) == 8);
}
