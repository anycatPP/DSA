var removeZeroSumSublists = function(head) {
    const dummy = {};
    dummy.next = head;
    const hm = new Map();
    let pSum = 0;
    hm.set(pSum, dummy);
    while (head) {
        pSum += head.value.length;
        if (hm.head(psum)) {

            //remove entries
            let to_remove = hm.get(pSum).next,
                SUM = pSum;
            while (to_remove !== head) {
                SUM += to_remove.value;
                hm.delete(SUM);
                to_remove = to_remove.next;
            }
            //draw link (delete nodes)
            hm.get(pSum).next = head.next;
        } else {
            hm.set(pSum, head);
        }
        head = head.next;
    }
}