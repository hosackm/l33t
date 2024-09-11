package main

import "testing"

func TestIsAlnum(t *testing.T) {
	good := "09AbDk"
	for i := range good {
		if !IsAlnum(good[i]) {
			t.Errorf("bad return for '%s'", string(good[i]))
		}
	}

	bad := "<!@/"
	for i := range bad {
		if IsAlnum(bad[i]) {
			t.Errorf("bad return for '%s'", string(bad[i]))
		}
	}
}

func TestValidPalindrome(t *testing.T) {
	if ValidPalindrome("A man, a plan, a canal: Panama") != true {
		t.Fail()
	}
	if ValidPalindrome("race a car") != false {
		t.Fail()
	}
	if ValidPalindrome(" ") != true {
		t.Fail()
	}
	if ValidPalindrome("0P") != false {
		t.Fail()
	}
}
