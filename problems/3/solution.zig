const testing = @import("std").testing;
const mem = @import("std").mem;

pub fn List(comptime T: type) type {
    return struct {
        const Self = @This();
        head: ?*Node = null,

        pub const Node = struct {
            const Self = @This();

            value: T,
            next: ?*Node = null,

            pub fn findLast(node: *Node) *Node {
                var it = node;
                while (true) {
                    it = it.next orelse return it;
                }
            }

            pub fn insertAfter(after: *Node, new_node: *Node) void {
                new_node.next = after.next;
                after.next = new_node;
            }

            pub fn countChildren(node: *Node) usize {
                var count: usize = 0;
                var it: ?*Node = node.next;
                while (it) |n| : (it = n.next) {
                    count += 1;
                }
                return count;
            }
        };

        pub fn append(list: *Self, new_node: *Node) void {
            new_node.next = list.head;
            list.head = new_node;
        }

        pub fn len(list: *Self) usize {
            if (list.head) |n| {
                return 1 + n.countChildren();
            } else {
                return 0;
            }
        }

        // User must free returned List
        pub fn merge(llist: *Self, rlist: *Self, empty: **Self) void {
            var left = llist.head;
            var right = rlist.head;
            var merged: Self = empty.*.*;
            var write: ?*Node = null;

            if (left == null) {
                merged.head = rlist.*.head;
                return;
            } else if (right == null) {
                merged.head = llist.*.head;
                return;
            } else {
                if (left.?.*.value < right.?.*.value) {
                    merged.head = left;
                    write = merged.head;
                    left = left.?.next;
                } else {
                    merged.head = right;
                    write = merged.head;
                    right = right.?.next;
                }
            }

            while (left != null and right != null) {
                if (left.?.*.value < right.?.*.value) {
                    write.?.next = left;
                    left = left.?.next;
                    write = write.?.next;
                } else {
                    write.?.next = right;
                    right = right.?.next;
                    write = write.?.next;
                }
            }
        }
    };
}

test "Can create and append List" {
    const L = List(i8);
    var list = L{};
    try testing.expect(list.head == null);

    var node = L.Node{ .value = 42 };
    list.append(&node);

    try testing.expect(list.head != null);
    try testing.expect(list.len() == 1);

    var node2 = L.Node{ .value = 100 };
    node.insertAfter(&node2);
    try testing.expect(list.len() == 2);

    try testing.expect(list.head.?.value == 42);
    try testing.expect(list.head.?.next.?.value == 100);
}

test "Merging" {
    const L = List(i8);
    var list1 = L{};
    var list2 = L{};
    var list3 = L{};
    var plist3 = &list3;

    const Node = L.Node;
    var n1 = Node{ .value = 1 };
    var n2 = Node{ .value = 2 };
    var n3 = Node{ .value = 3 };
    var n4 = Node{ .value = 4 };
    var n5 = Node{ .value = 5 };
    var n6 = Node{ .value = 6 };
    var n7 = Node{ .value = 7 };

    list1.append(&n1);
    list1.append(&n2);
    list1.append(&n3);
    list1.append(&n4);

    list2.append(&n5);
    list2.append(&n6);
    list2.append(&n7);

    list1.merge(&list2, &plist3);
}
