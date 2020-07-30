Feature: Smoke test

  @smoketest
  Scenario: Check the function int add(int, int)
    Given The library libadder.so is loaded
    When I call native function add with integer arguments 1 and 2
    Then I should get 3 as a result

  Scenario Outline: Thorough checking function int add(int, int)
    Given The library libadder.so is loaded
    When I call native function add with integer arguments <x> and <y>
    Then I should get <result> as a result

     Examples: results
     |x|y|result|
     # basic arithmetic
     |          0| 0|          0|
     |          1| 2|          3|
     |          1|-2|         -1|
     # no overflows at 16 bit limits
     |      32767| 1|      32768|
     |      65535| 1|      65536|
     # integer overflow
     | 2147483648| 1|-2147483647|
     |-2147483647|-1|-2147483648|
     |-2147483648|-1| 2147483647|

